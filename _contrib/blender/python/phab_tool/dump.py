from collections import defaultdict
import dataclasses
import datetime
import logging
from pathlib import Path
from typing import Any, Callable, Iterable

from slugify import slugify

import phabricator
from phabricator import Phabricator

import urllib.request

from . import common


@dataclasses.dataclass
class ResumeInfo:
    """Info needed to resume after operations were stopped.

    This includes modification timestamps of last-seen Phabricator objects, and
    numbers of last-visited objects (like task/diff numbers) when modification
    timestamps are unavailable/unusable.
    """

    __file = common.orig_dir / "resume-info.json"

    # Timestamps, in local UNIX timestamp.
    manifest: int = 0  # dateModified of last-handled task.
    differential: int = 0  # dateModified of last-handled DREV object
    file: int = 0  # dateModified of last-handled file.

    # Last-handled object numbers (T/D-numbers).
    manifest_last_id: int = 0
    task_transaction: int = 0
    task_edge: int = 0
    drev_transaction: int = 0
    drev_diff: int = 0

    # UNIX timestamp of when the last `pt_manifest_update` call was started.
    manifest_last_update_timestamp: int = 0

    def save(self) -> None:
        log.info("Saving last-modification to %s", self.__file)
        if self.__file.exists():
            bak_path = self.__file.with_name(self.__file.name + "~")
            self.__file.rename(bak_path)
        common.saveJsonFile(dataclasses.asdict(self), self.__file)

    @classmethod
    def load(cls) -> "ResumeInfo":
        log.info("Loading last-modification from %s", cls.__file)
        try:
            last_mod_data = common.readJsonFile(cls.__file)
        except FileNotFoundError:
            log.warning("File %s not found, going to start from scratch", cls.__file)
            return ResumeInfo()

        return ResumeInfo(**last_mod_data)

    @staticmethod
    def inspect(path: Path) -> int:
        """Iterate over all JSON files in 'path' and return the latest `dateModified` field."""
        log.info("Inspecting already-dumped data to find last modification: %s", path)

        max_date_mod = 0
        for fpath in path.glob("**/*.json"):
            task_mod = dumped_task_date_modified(fpath)
            max_date_mod = max(max_date_mod, task_mod)

        log.info(
            "Last modification date found in %s: %s",
            path,
            common.humanize_timestamp(max_date_mod),
        )
        return max_date_mod


last_mod = ResumeInfo()

log = logging.getLogger(__name__)

# Mapping from PHID-TASK-xxx to its number.
task_phid_to_number: dict[str, int] = {}
# This cannot be in common.orig_dirs["task"] because the code assumes that all
# JSON files in there are task dicts.
_task_phid_to_number_path = common.orig_dir / "task-phid-to-number.json"


def saveState():
    last_mod.save()
    common.saveJsonFile(task_phid_to_number, _task_phid_to_number_path)


def restoreState():
    """Populate data structures to resume dumps from previous runs."""
    global last_mod, task_phid_to_number
    last_mod = ResumeInfo.load()

    if _task_phid_to_number_path.exists():
        task_phid_to_number = common.readJsonFile(_task_phid_to_number_path)


def pt_dump(phab: Phabricator) -> None:
    log.warning("This only dumps the fast-to-dump stuff, not everything!")

    pt_dump_projects(phab)
    pt_dump_repositories(phab)

    log.warning("This only dumped the fast-to-dump stuff, not everything!")


def pt_dump_maniphest(phab: Phabricator) -> None:
    """Dump all Phabricator tasks to JSON, by last modification."""
    num_issues = 0
    page_size = 100  # query 100 items at a time.

    if not last_mod.manifest:
        last_mod.manifest = last_mod.inspect(common.orig_dirs["task"])
        last_mod.save()

    # Remember IDs we've seen in the last iteration, to prevent duplicates.
    last_iteration_ids: set[int] = set()
    while True:
        # Start querying from the last-seen modification. Phabricator will give
        # us the last-seen object again, but this is necessary to ensure we
        # don't skip anything (like tasks with the same last-mod timestamp that
        # are each on another side of the limit=page_size edge.)
        modified_start = last_mod.manifest

        log.info(
            "Getting issues modified since %d (%s)",
            modified_start,
            common.humanize_timestamp(modified_start),
        )

        query_args = dict(
            constraints={"modifiedStart": modified_start},
            order="outdated",  # "outdated" means "by modification, oldest first".
            limit=page_size,
            attachments={
                "columns": True,  # Workboard Columns
                "subscribers": True,
                "projects": True,
            },
        )
        result = phab.maniphest.search(**query_args)

        if not result.data:
            break

        this_iteration_ids: set[int] = set()
        for task in result.data:
            task_id = int(task["id"])

            this_iteration_ids.add(task_id)
            if task_id in last_iteration_ids:
                log.info("Skipping T%d (we've seen it in the previous query)", task_id)
                continue

            _dump_task_with_transactions(phab, task)

            last_mod.manifest = max(last_mod.manifest, task["fields"]["dateModified"])
            num_issues += 1

        if len(result.data) == page_size and last_iteration_ids == this_iteration_ids:
            # This was a full page of data, but we've seen all these IDs before.
            # That means we've hit a modification timestamp that is shared by
            # more than `page_size` tasks. Phabricator cannot deal with this.
            log.error(
                f"We've seen the same {len(this_iteration_ids)} tasks two {page_size}-task iterations in a row, "
                f"with last-mod >= {modified_start} ({common.humanize_timestamp(modified_start)})"
            )
            raise RuntimeError("Hitting limitation of Phabricator API")

        if last_iteration_ids == this_iteration_ids:
            # We've seen all of these already, and this was not a full page of data, so we're done.
            break

        last_iteration_ids = this_iteration_ids

    log.info("Processed %d issues, all done.", num_issues)


def pt_dump_maniphest_all(phab: Phabricator) -> None:
    """Dump all maniphest tasks, by ID.

    This is necessary because in 2019-12-23 15:35:42 UTC (unix timestamp
    2019-12-23 15:35:42 UTC) there were more than 100 tasks changed on the same
    timestamp. And the Phabricator API doesn't make it possible to fetch those
    based on last-mod timestamp. A full dump MUST be done by ID.
    """
    log.info("Downloading all maniphest tasks")

    after = last_mod.manifest_last_id or None  # 0 is not valid for Phabricator.

    # Find the last task ID so we can guesstimate the time left.
    result = phab.maniphest.search(order="newest", limit=1)
    if result.data:
        last_task_id = result.data[0]["id"]
    else:
        last_task_id = 103916  # this is the last task at the moment of writing
        log.warning("unable to get last task ID, doing a guess it's T%d", last_task_id)
    num_tasks_to_dump = last_task_id if after is None else (last_task_id - after)

    def iter_tasks():
        for result in _iter_paged(
            phab.maniphest.search,
            order="oldest",
            limit=100,
            after=after,
            attachments={
                "columns": True,  # Workboard Columns
                "subscribers": True,
                "projects": True,
            },
        ):
            for task in result.data:
                yield task

    num_tasks = 0
    for task in common.timed_iter(log, iter_tasks(), num_tasks_to_dump):
        _dump_task_with_transactions(phab, task)
        num_tasks += 1
        last_mod.manifest_last_id = task["id"]

    log.info("Done, dumped %d tasks", num_tasks)


def pt_dump_maniphest_update(phab: Phabricator) -> None:
    """Update maniphest tasks, but only ones mentioned in `./tasks.py`.

    Incrementally update maniphest tasks, given a list of specific tasks to
    re-dump.
    """

    time_start = datetime.datetime.utcnow()

    updated_tasks = common.readJsonFile("tasks.json")
    log.info("Downloading %d maniphest tasks", len(updated_tasks))

    # Iterate over chunks of tasks instead of querying one by one.
    chunksize = 10
    chunks = [
        updated_tasks[i : i + chunksize]
        for i in range(0, len(updated_tasks), chunksize)
    ]

    log.info(
        "NOTE: the tasks are downloaded in chunks. Progress info is about chunks of %d tasks each.",
        chunksize,
    )

    num_tasks = 0
    for task_ids in common.timed_iter(log, chunks):
        query_args = dict(
            constraints={"ids": task_ids},
            order="oldest",
            limit=100,
            attachments={
                "columns": True,  # Workboard Columns
                "subscribers": True,
                "projects": True,
            },
        )
        result = phab.maniphest.search(**query_args)

        for task in result.data:
            _dump_task_with_transactions(phab, task)
            num_tasks += 1

    last_mod.manifest_last_update_timestamp = int(time_start.timestamp())

    log.info(
        "Done, dumped %d tasks. New timecode for future updates is %d",
        num_tasks,
        last_mod.manifest_last_update_timestamp,
    )


def _dump_task_with_transactions(phab: Phabricator, task: dict[str, Any]) -> None:
    task_id: int = task["id"]
    assert isinstance(task_id, int), f"expecting task IDs to be int, got {task_id!r}"

    task_phid_to_number[task["phid"]] = task_id

    json_subpath = common.subpath(task_id, ".json")
    task_json_path = common.orig_dirs["task"] / json_subpath
    log.info("Dumping T%d: %s", task_id, task["fields"]["name"])

    # Fetch the transactions of this task.
    trans_json_path = common.orig_dirs["xact-task"] / json_subpath
    transactions = _load_transactions(phab, task["phid"])

    # Fetch the 'edges' of this task, i.e. relations with other Phabricator objects.
    edge_json_path = common.orig_dirs["edge-task"] / json_subpath
    edges = _load_task_edges(phab, task["phid"])

    # Only save to disk after we've downloaded everything.
    common.saveJsonFile(transactions, trans_json_path)
    if edges:
        common.saveJsonFile(edges, edge_json_path)
    else:
        edge_json_path.unlink(missing_ok=True)
    common.saveJsonFile(task, task_json_path)


def pt_dump_maniphest_transactions(phab: Phabricator) -> None:
    """Refresh transactions of already-downloaded maniphest tasks."""
    log.info("Refreshing maniphest task transactions")

    paths = sorted(
        path
        for path in common.orig_dirs["task"].glob("**/*.json")
        if int(path.stem) > last_mod.task_transaction
    )

    for task_json_path in common.timed_iter(log, paths):
        # Figure out the task PHID:
        task_data = common.readJsonFile(task_json_path)
        task_phid = task_data["phid"]

        # Refresh the transactions.
        json_subpath = common.subpath(task_data["id"], ".json")
        trans_json_path = common.orig_dirs["xact-task"] / json_subpath
        transactions = _load_transactions(phab, task_phid)
        common.saveJsonFile(transactions, trans_json_path)

        last_mod.task_transaction = int(task_json_path.stem)


def pt_dump_maniphest_edges(phab: Phabricator) -> None:
    """Refresh edges of already-downloaded maniphest tasks."""
    log.info("Refreshing maniphest task edges")

    paths = sorted(
        path
        for path in common.orig_dirs["task"].glob("**/*.json")
        if int(path.stem) > last_mod.task_edge
    )

    for task_json_path in common.timed_iter(log, paths):
        # Figure out the task PHID:
        task_data = common.readJsonFile(task_json_path)
        task_phid = task_data["phid"]

        # Refresh the edges.
        json_subpath = common.subpath(task_data["id"], ".json")
        edge_json_path = common.orig_dirs["edge-task"] / json_subpath
        edges = _load_task_edges(phab, task_phid)
        if edges:
            common.saveJsonFile(edges, edge_json_path)
        else:
            edge_json_path.unlink(missing_ok=True)

        last_mod.task_edge = int(task_json_path.stem)


def pt_dump_differential(phab: Phabricator) -> None:
    """Dump all differential revisions to JSON."""
    num_dumped = 0

    dump_path = common.orig_dirs["drev"]
    transactions_path = common.orig_dirs["xact-drev"]

    if not last_mod.differential:
        last_mod.differential = last_mod.inspect(dump_path)
        last_mod.save()

    while True:
        # Start querying from the last-seen modification + 1 second. Otherwise
        # Phabricator will give us the last-seen object again.
        modified_start = last_mod.differential + 1

        log.info(
            "Getting differentials modified since %s",
            common.humanize_timestamp(modified_start),
        )

        # Grab all diffs, because plenty will not be tagged with the Blender project.
        result = phab.differential.revision.search(
            constraints={
                "modifiedStart": modified_start,
            },
            order="outdated",  # "outdated" means "by modification, oldest first".
            limit=100,
            attachments={
                "reviewers": True,
                "subscribers": True,
                "projects": True,
            },
        )

        if not result.data:
            break

        for drev in result.data:
            drev_id: int = drev["id"]
            drev_phid: str = drev["phid"]

            log.info("Dumping D%d: %s", drev_id, drev["fields"]["title"])

            _dump_phab_diffs(phab, drev_id, drev_phid)

            transactions = _load_transactions(phab, drev_phid)

            json_subpath = common.subpath(drev_id, ".json")
            common.saveJsonFile(transactions, transactions_path / json_subpath)
            common.saveJsonFile(drev, dump_path / json_subpath)

            last_mod.differential = max(
                last_mod.differential, drev["fields"]["dateModified"]
            )
            num_dumped += 1

    log.info("Processed %d revisions, all done.", num_dumped)


def pt_dump_differential_transactions(phab: Phabricator) -> None:
    """Refresh transactions of already-downloaded differential revisions.

    This is intended to be used as a last step to be sure that transaction
    changes that do NOT change the differential's `dateModified` field are still
    included in the dump.
    """
    log.info("Refreshing differential revision transactions")

    paths = sorted(
        path
        for path in common.orig_dirs["drev"].glob("**/*.json")
        if int(path.stem) > last_mod.drev_transaction
    )

    for drev_json_path in common.timed_iter(log, paths):
        # Figure out the drev PHID:
        drev_data = common.readJsonFile(drev_json_path)
        drev_phid = drev_data["phid"]

        # Refresh the transactions.
        json_subpath = common.subpath(drev_data["id"], ".json")
        transactions = _load_transactions(phab, drev_phid)
        common.saveJsonFile(transactions, common.orig_dirs["xact-drev"] / json_subpath)

        last_mod.drev_transaction = int(drev_json_path.stem)


def pt_dump_differential_diffs(phab: Phabricator) -> None:
    """Of the already-downloaded DREVs, dump their DIFFs and raw diff files."""
    log.info("Refreshing differential revision diffs")

    paths = sorted(
        path
        for path in common.orig_dirs["drev"].glob("**/*.json")
        if int(path.stem) > last_mod.drev_diff
    )

    for drev_json_path in common.timed_iter(log, paths):
        # Figure out the drev PHID:
        drev_data = common.readJsonFile(drev_json_path)
        drev_phid: str = drev_data["phid"]
        drev_id: int = drev_data["id"]

        _dump_phab_diffs(phab, drev_id, drev_phid)
        last_mod.drev_transaction = int(drev_json_path.stem)

    # TODO: move generating diff stats to the `debug` module (and maybe rename
    # that to `meta` or something like that).
    #
    #     # we update some stat-related stuff
    #     dstats["status"] = drev["fields"]["status"]  #  Save status in stats
    #     dstats["phid"] = drev["phid"]  # save phid in stats
    #     # We iterate over the diffs, keep a count of the total found , and how many of them were 'empty. If count=empty_count, set 'baseless' to true, else false
    #     count = 0
    #     empty_count = 0
    #     for mydiff in diffs.data:
    #         count = count + 1
    #         if len(mydiff["fields"]["refs"]) == 0:
    #             empty_count = empty_count + 1
    #     if empty_count == count:
    #         dstats["baseless"] = True
    #     else:
    #         dstats["baseless"] = False
    #     dstats["refs_total"] = count
    #     dstats["refs_empty"] = empty_count
    #     # stats[drev_number] = dstats

    # # Before we are done with all of this, we save our stats
    # common.saveJsonFile(dstats, "diffs-stats.json")


def pt_dump_projects(phab: Phabricator) -> None:
    """Dump projects and their workboards."""
    log.info("Dumping projects")

    projects = _load_paged(
        phab.project.search,
        constraints={},
        order="oldest",
        limit=100,
        attachments={
            "members": True,
            "watchers": True,
            "ancestors": True,
        },
    )

    seen_slugs = defaultdict(int)

    for proj in projects:
        slug = proj["fields"]["slug"]
        proj["fields"]["_phab_slug"] = slug

        if not slug:
            # Not all projects have a slug.
            slug = slugify(proj["fields"]["name"])

        # Make sure slugs are unique.
        seen_slugs[slug] += 1
        while seen_slugs[slug] > 1:
            slug = f"{slug}-{seen_slugs[slug]}"
            seen_slugs[slug] += 1

        proj["fields"]["slug"] = slug

    json_path = common.orig_dir / "projects.json"
    log.info("Fetched %d projects, writing to %s", len(projects), json_path)
    common.saveJsonFile(projects, json_path)


def dumped_task_date_modified(task_path: Path) -> int:
    """Load task JSON, and return its `dateModified` field.

    Return 0 when the path does not exist.
    """

    try:
        task = common.readJsonFile(task_path)
    except FileNotFoundError:
        return 0
    assert isinstance(task, dict)

    dateModified: int = task["fields"]["dateModified"]
    return dateModified


def _load_paged(
    search_func: Callable[..., Any],
    /,
    *args: Iterable[Any],
    **kwargs: Any,
) -> list[dict[str, Any]]:
    """Load all pages of search results."""
    results = []
    after = None

    while True:
        page = search_func(*args, **kwargs, after=after)

        results.extend(page.data)

        after = page.cursor["after"]
        if not after:
            break

    return results


def _iter_paged(
    search_func: Callable[..., Any],
    /,
    after: int | None = None,
    *args: Iterable[Any],
    **kwargs: Any,
) -> Iterable[phabricator.Result]:
    """Generator, goes over pages of search results."""

    while True:
        page = search_func(*args, **kwargs, after=after)

        if not page.data:
            break

        yield page

        after = page.cursor["after"]
        if not after:
            break


def _load_transactions(phab: Phabricator, owner_phid: str) -> list[dict[str, Any]]:
    """Load all transactions.

    Phabricator transactions are actually mutable. Editing a comment adds a new
    entry to the transaction that created the comment. The transaction ID is
    kept the same, but the `dateModified` field is updated. Unfortunately there
    is no way to query for transactions since a certain timestamp.
    """
    return _load_paged(
        phab.transaction.search,
        objectIdentifier=owner_phid,
        constraints={},
        limit=100,
    )


def _load_task_edges(phab: Phabricator, owner_phid: str) -> list[dict[str, Any]]:
    edges = _load_edges(
        phab,
        owner_phid,
        {
            # Just grab all task-related edges. Not all are handled by the
            # conversion script, but at least if we want to add support we
            # won't have to redownload everything.
            "task.commit",
            "task.duplicate",
            "task.merged-in",
            "task.parent",
            "task.revision",
            "task.subtask",
        },
    )
    if not edges:
        return []

    # Group the edges per type, so they can be queried in one go.
    edges_per_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for edge in edges:
        edges_per_type[edge["edgeType"]].append(edge)

    # Enrich with extra info from Phabricator, as the edge itself is really just
    # "from PHID-A to PHID-B".
    _edges_fetch_commits(phab, edges_per_type["task.commit"])

    return edges


def _load_edges(
    phab: Phabricator, owner_phid: str, edge_types: set[str]
) -> list[dict[str, Any]]:
    """Load edges of Phab objects.

    These are the relations between objects (like tasks & commits).
    See https://developer.blender.org/conduit/method/edge.search/ for the edge types.
    """
    return _load_paged(
        phab.edge.search,
        sourcePHIDs=[owner_phid],
        types=list(edge_types),
        limit=100,
    )


def _edges_fetch_commits(phab: Phabricator, edges: list[dict[str, Any]]) -> None:
    """Fetch the commits pointed to by the edges."""
    if not edges:
        return

    commit_phids: list[str] = [edge["destinationPHID"] for edge in edges]

    commits = _load_paged(
        phab.diffusion.commit.search,
        constraints={"phids": commit_phids},
    )

    for commit in commits:
        edge_idx = commit_phids.index(commit["phid"])
        edges[edge_idx]["commit"] = commit


def _load_revision_diffs(phab: Phabricator, drev_phid: str) -> list[dict[str, Any]]:
    return _load_paged(
        phab.differential.diff.search,
        constraints={"revisionPHIDs": [drev_phid]},
        order="oldest",
        limit=100,
        attachments={"commits": True},
    )


def _dump_phab_diffs(
    phab: Phabricator,
    drev_id: int,
    drev_phid: str,
) -> None:
    """Given a DREV, dump its DIFF objects and raw diff files."""
    diff_dir = common.orig_dirs["diff"] / common.subpath(drev_id)

    diffs = _load_revision_diffs(phab, drev_phid)
    _dump_raw_diffs(phab, drev_id, diffs, diff_dir)
    common.saveJsonFile(diffs, diff_dir / "metadata.json")


def _dump_raw_diffs(
    phab: Phabricator,
    drev_id: int,
    phab_diffs: list[dict[str, Any]],
    raw_diff_dir: Path,
) -> None:
    """Download the raw diffs of this DREV.

    Skips diff files that we have already downloaded.

    :param phab_diffs: Phab DIFF objects, from _load_revision_diffs().
    """

    for diff in phab_diffs:
        diff_id = int(diff["id"])

        raw_diff_path = raw_diff_dir / f"{diff_id:07}.diff"
        if raw_diff_path.exists() and raw_diff_path.stat().st_size > 0:
            continue

        result = phab.differential.getrawdiff(diffID=str(diff_id))

        log.info("D%d: Saving raw patch %s", drev_id, raw_diff_path)
        common.saveTextFile(result.response, raw_diff_path)


def _get_last_stored_file_id() -> int:
    parent_dirs = sorted(
        common.orig_dirs["file"].iterdir(), key=lambda path: int(path.name)
    )
    if not parent_dirs:
        return 0

    last_dir = parent_dirs[-1]

    last_files = sorted(last_dir.iterdir())

    return int(last_files[-1].stem)


def _get_last_file_id(phab: Phabricator) -> int:
    """Get ID of the newest file. Files up to this ID will be queried and downloaded"""

    # Technically, the limit could be 1, but in reality it was causing some weird
    # artifacts when no files were found at all while the Phabricator was indexing
    # new commits.
    result = phab.file.search(
        order="newest",
        limit=100,
    )

    if not result.data:
        raise Exception("Unable to query last file ID")

    return int(result.data[0]["id"])


def _compile_file_info_and_search_result_to_dict(
    file_info_result: dict, file_search_info: dict
) -> dict:
    """
    Combine result of two queries into single dict with all information

    NOTE: Caller must convert the API result to dictionary
    """

    file = dict(file_info_result)

    file["type"] = file_search_info["type"]
    file["dataURI"] = file_search_info["fields"]["dataURI"]
    file["policy"] = file_search_info["fields"]["policy"]

    return file


def get_file_info(phab: Phabricator, id: int) -> phabricator.Result | None:
    """
    Failure safe way to retrieve information about file
    """

    try:
        return phab.file.info(id=id)
    except phabricator.APIError as e:
        if e.code == "ERR-NOT-FOUND":
            log.info(
                "Ignoring F%d: File not found (removed temporary file?)",
                id,
            )
            return None
        elif e.code == "ERR-CONDUIT-CORE":
            # Assume this is an access denied due to the view restrictions on the file.
            # Can verify this by checking error_info for the `[Access Denied: Restricted File]` substring.
            log.info(
                "Ignoring F%d: Seems to have restricted visibility",
                id,
            )
            return None
        else:
            raise e


def is_preview_file(phab: Phabricator, info_result: phabricator.Result) -> bool:
    """
    Check whether the info_result denotes file which is a preview transform for another file
    """

    if not info_result["name"].startswith("preview-"):
        return False

    return True


def pt_dump_files(phab: Phabricator) -> None:
    """Dump all Phabricator files to JSON and actual files on disk."""

    meme_file_ids = (
        14197163,
        14205963,
    )

    num_files = 0

    if not last_mod.file:
        last_mod.file = _get_last_stored_file_id() + 1
        last_mod.save()

    last_file_id = _get_last_file_id(phab)
    log.info("Processing files up to ID %d", last_file_id)

    for current_file_id in range(last_mod.file, last_file_id + 1):
        if current_file_id < last_mod.file:
            continue

        json_subpath = common.subpath(current_file_id, ".json")
        file_json_path = common.orig_dirs["file"] / json_subpath

        file_data_subpath = common.subpath(current_file_id, "")
        file_data_path = common.orig_dirs["file_data"] / file_data_subpath

        if file_json_path.exists() and file_data_path.exists():
            log.info("Skipping file ID %d", current_file_id)
            continue

        log.info(
            "Getting information for file ID %d",
            current_file_id,
        )

        file_info_result = get_file_info(phab, current_file_id)
        if not file_info_result:
            last_mod.file = current_file_id + 1
            continue

        if not file_info_result["authorPHID"] and current_file_id not in meme_file_ids:
            if not is_preview_file(phab, file_info_result):
                log.info(
                    "Ignoring F%d: Seems to be automatically generated internal file",
                    current_file_id,
                )
                last_mod.file = current_file_id + 1
                continue

        log.info("Dumping F%d: %s", current_file_id, file_info_result["name"])

        file_search_result = phab.file.search(
            constraints={
                "ids": [current_file_id],
            },
        )

        assert file_search_result.data

        file = _compile_file_info_and_search_result_to_dict(
            dict(file_info_result), dict(file_search_result.data[0])
        )

        file_data_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            urllib.request.urlretrieve(file["dataURI"], file_data_path)
        except urllib.error.HTTPError as e:
            if e.code == 500:
                log.info(
                    "Ignoring F%d: File was removed from disk",
                    current_file_id,
                )
                continue
            if e.code == 404:
                log.info(
                    "Ignoring missing file F%d",
                    current_file_id,
                )
                continue
            raise e

        common.saveJsonFile(file, file_json_path)

        last_mod.file = current_file_id + 1

    log.info("Processed %d files, all done.", num_files)


def _get_last_paste_id(phab: Phabricator) -> int:
    """Get ID of the newest paste. Pastes up to this ID will be queried and downloaded"""

    result = phab.paste.search(
        order="newest",
        limit=1,
    )

    if not result.data:
        raise Exception("Unable to query last paste ID")

    return int(result.data[0]["id"])


def pt_dump_pastes(phab: Phabricator) -> None:
    """Dump all Phabricator pastes to JSON."""
    num_pastes = 0

    last_paste_id = _get_last_paste_id(phab)
    log.info("Processing files up to ID %d", last_paste_id)

    last_handled_paste_id = 0
    while last_handled_paste_id < last_paste_id:
        log.info(
            "Getting pastes after ID %d",
            last_handled_paste_id,
        )

        after_id = last_handled_paste_id + 1

        try:
            # Lower the limit to avoid server timeout issues.
            result = phab.paste.search(
                order="oldest",
                limit=10,
                attachments={
                    "content": True,
                },
                after=None if last_handled_paste_id == 0 else after_id,
            )
        except phabricator.APIError as e:
            # The Conduit API expects that "after" is a valid identifier. If the paste is removed, then an error will
            # be returned. In this case just move to the next ID and try again.
            if e.code == "ERR-CONDUIT-CORE":
                if "does not identify a valid object in query" in e.message:
                    log.info("Ignoring non-existing P%d", after_id)
                    last_handled_paste_id += 1
                    continue
                if "Access Denied: Restricted Paste" in e.message:
                    log.info("Ignoring restricted P%d", after_id)
                    last_handled_paste_id += 1
                    continue
            raise e

        if not result.data:
            break

        for paste in result.data:
            paste_id = int(paste["id"])

            json_subpath = common.subpath(paste_id, ".json")
            paste_json_path = common.orig_dirs["paste"] / json_subpath
            log.info("Dumping P%d: %s", paste_id, paste["fields"]["title"])

            common.saveJsonFile(paste, paste_json_path)

            last_handled_paste_id = paste_id

    log.info("Processed %d pastes, all done.", num_pastes)


def pt_dump_repositories(phab: Phabricator) -> None:
    """Dump info about Phabricator repositories."""

    log.info("Dumping repositories")

    repos = _load_paged(
        phab.diffusion.repository.search,
        attachments=["uris", "metrics", "projects"],
    )

    json_path = common.orig_dirs["repo"] / "diffusion.json"
    log.info("Fetched %d repositories, writing to %s", len(repos), json_path)
    common.saveJsonFile(repos, json_path)


def update_task_phid_to_number_mapping() -> None:
    """Populate task_phid_to_number with on-disk tasks.

    Only needed once, so I didn't bother creating a py.blabla link.
    """
    log.info("Populating task PHID to number mapping")

    restoreState()

    paths = sorted(common.orig_dirs["task"].glob("**/*.json"))

    known_task_numbers = set(task_phid_to_number.values())

    for task_json_path in common.timed_iter(log, paths):
        taskid_from_file = int(task_json_path.stem)
        if taskid_from_file in known_task_numbers:
            # Don't bother parsing known PHIDs.
            continue

        task_data = common.readJsonFile(task_json_path)
        phid = task_data["phid"]
        task_id = task_data["id"]
        assert isinstance(task_id, int), f"expected int, got {task_id!r}"
        assert task_id == taskid_from_file
        task_phid_to_number[phid] = task_id

    saveState()


def invalid_subscribers_to_tasks_json(phab: Phabricator) -> None:
    tasks_with_invalid_subscribers = []

    for task_json_path in common.orig_dirs["task"].glob("**/*.json"):
        task_data = common.readJsonFile(task_json_path)
        subscribers = task_data.get("attachments", {}).get("subscribers", {})

        subscriberCount = subscribers.get("subscriberCount", 0)
        subscriberPHIDs = subscribers.get("subscriberPHIDs", [])

        if subscriberCount != len(subscriberPHIDs):
            tasks_with_invalid_subscribers.append(int(task_data["id"]))

    common.saveJsonFile(tasks_with_invalid_subscribers, "tasks.json")
