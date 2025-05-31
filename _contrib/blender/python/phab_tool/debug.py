import logging
from pathlib import Path

from phabricator import Phabricator

from . import common, convert, users
from .convert import transactions as conv_trans
from .convert import heuristics


_log = logging.getLogger(__name__)


def pt_debug_differential_diffs_stats(phab: Phabricator) -> None:
    """Iterate over all DREVs we have, combine it with data in associated DIFF object to produce a STATS file"""

    stats = {}

    for drev_file in sorted(Path(common.orig_dirs["pull_request"]).glob("*.json")):
        drev_number = int(drev_file.stem)
        stats[drev_number] = {}
        dstats = stats[drev_number] = {}

        drev = common.readJsonFile(drev_file)
        diffs = common.readJsonFile("orig/diffs/%07d.json" % drev_number)
        dstats["status"] = drev["fields"]["status"]
        dstats["phid"] = drev["phid"]
        count = 0
        empty_count = 0
        for mydiff in diffs:
            count = count + 1
            if len(mydiff["fields"]["refs"]) == 0:
                empty_count = empty_count + 1
        if empty_count == count:
            dstats["baseless"] = True
        else:
            dstats["baseless"] = False
        dstats["refs_total"] = count
        dstats["refs_empty"] = empty_count

    common.saveJsonFile(stats, "diffs-stats.json")


def pt_debug_users_prune(phab: Phabricator) -> None:
    """Remove unreferenced JSON files from data/orig/user.

    Since we won't be converting all tasks (f.e. spam tasks are ignored) and no
    differential revisions, the list of referenced users can be trimmed down.
    """

    _log.info("Investigating tasks")

    issue_paths = sorted(common.orig_dirs["task"].glob("**/*.json"), reverse=True)
    path_xact_task = common.orig_dirs["xact-task"]

    # Monkey-patch the user module so we can track which users are looked up.
    orig_getUser = users.getBestEffortUser
    orig_loglevel = conv_trans._log.getEffectiveLevel()
    requested_phids: set[str] = set()

    def patched_getUser(phab: Phabricator, userPhid: str) -> users.BestEffortUser:
        requested_phids.add(userPhid)
        return orig_getUser(phab, userPhid)

    try:
        users.getBestEffortUser = patched_getUser
        conv_trans._log.setLevel(logging.ERROR)

        # NOTE: this was copied from phab_tool.convert.pt_convert_maniphest() and
        # stripped of anything that writes to disk.
        for issue_file in common.timed_iter(_log, issue_paths):
            task = common.readJsonFile(issue_file)
            task_id = task["id"]
            assert isinstance(task_id, int)

            ctx = heuristics.task_context(task)
            if ctx.reject or not ctx.repository:
                continue

            trans_file = path_xact_task / common.subpath(task_id, ".json")
            convert.taskConvertToGitea(phab, task, ctx)
            conv_trans.convertToGitea(
                phab, common.readJsonFile(trans_file), task_id, ctx
            )
    finally:
        users.getBestEffortUser = orig_getUser
        conv_trans._log.setLevel(orig_loglevel)

    _log.info("Task conversion touched %d users", len(requested_phids))

    num_removed_paths = 0
    user_json_paths = list(common.orig_dirs["user"].glob("**/*.json"))
    for user_path in user_json_paths:
        user_phid = user_path.stem
        if user_phid in requested_phids:
            continue
        user_path.unlink()
        num_removed_paths += 1

    _log.info(
        "Removed %d of %d user JSON files", num_removed_paths, len(user_json_paths)
    )
