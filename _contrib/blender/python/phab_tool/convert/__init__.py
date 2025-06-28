import sys
from pathlib import Path
from typing import Any
import dataclasses
import logging

from phabricator import Phabricator

from .. import common, users, parallel
from . import gitea_types as gt
from . import transactions as conv_trans
from . import paths, orgs_and_repos, heuristics, tracability, user_mapping, phab_tasks
from . import markup_processor


# TODO: these need to become organisation/repo aware.
issues_dir = paths.convert_dir / "issues"
comments_dir = paths.convert_dir / "comments"
pull_requests_dir = paths.convert_dir / "pull_requests"

log = logging.getLogger(__name__)

# Set of all the labels that have been generated, so that they can be written to `labels.yml`.
label_gatherer = orgs_and_repos.LabelGatherer()
labels_for_task_subtype = {
    "bug": "Type::Bug",
    "default": "Type::Report",
    "design": "Type::Design",
    "knownissue": "Type::Known Issue",
    "patch": "Type::Patch",
    "todo": "Type::To Do",
}

task_tracer = tracability.TaskTracer()


def pt_convert(phab: Phabricator) -> None:
    orgs_and_repos.ensure_orgs_on_gitea()
    orgs_and_repos.create_repo_dirs_for_conversion()
    pt_convert_maniphest(phab)


def pt_convert_maniphest(phab: Phabricator) -> None:
    """Convert manifest tasks into Gitea issues."""
    log.info("Converting manifest tasks to Gitea issues")

    # Load users outside of the `timed_iter()` loop to avoid skewing the timings.
    users.loadUserData()

    path_xact_task = common.orig_dirs["xact-task"]
    path_edge_task = common.orig_dirs["edge-task"]

    issue_paths = sorted(common.orig_dirs["task"].glob("**/*.json"), reverse=True)
    limit_repos = set(sys.argv[1:])

    # For testing, limit to latest few tasks.
    # issue_paths = sorted(issue_paths[:4000])
    # issue_paths = [p for p in issue_paths if "103937" in str(p)]

    # First stage: load all tasks and determine where they go in Gitea. This is
    # necessary to resolve merged tasks, especially those where a newer task is
    # merged into an older one: converting the older task requires knowledge of
    # the newer task.
    log.info("--------- stage 1: Loading all tasks")
    skip_task_ids: set[int] = set()
    for issue_file in common.timed_iter(log, issue_paths):
        task = phab_tasks.load(issue_file)
        task_id = task["id"]
        assert isinstance(task_id, int)

        ctx = heuristics.task_context(task)
        if ctx.reject:
            log.debug("Rejecting T%d", task_id)
            skip_task_ids.add(task_id)
            continue

        if not ctx.repository:
            log.warning("Task T%d has no Gitea repository, skipping", task_id)
            skip_task_ids.add(task_id)
            continue

        task_tracer.add(task_id, ctx.repository)

    # Second stage: actually convert the tasks.
    log.info("--------- stage 2: Converting tasks")
    with parallel.OutputGatherer(log) as gather:
        for issue_file in common.timed_iter(log, issue_paths):
            task = phab_tasks.load(issue_file)
            task_id = task["id"]
            if task_id in skip_task_ids:
                continue  # The reason why is already logged

            ctx = heuristics.task_context_of_phid(task["phid"])
            if limit_repos and ctx.repository not in limit_repos:
                log.debug("Skipping T%d, it is in repo %s", task_id, ctx.repository)
                continue

            gitea_issue = taskConvertToGitea(phab, task, ctx)
            yaml_issue_path = paths.for_issues_yaml(ctx)
            gather.append_as_yaml([dataclasses.asdict(gitea_issue)], yaml_issue_path)

            # Handle the comments of this task. These can be both transactions
            # and "edges", i.e. relations to other Phabricator objects.
            trans_file = path_xact_task / common.subpath(task_id, ".json")
            edge_file = path_edge_task / common.subpath(task_id, ".json")
            yaml_comments_path = paths.for_issue_comments_yaml(ctx, task_id)

            comments = conv_trans.convertToGitea(
                phab, common.readJsonFile(trans_file), task_id, ctx
            )

            if edge_file.exists():
                edge_comments = conv_trans.convert_edges(
                    phab, common.readJsonFile(edge_file), task_id, ctx
                )
                comments.extend(edge_comments)

            _ensure_comment_timestamp(task, comments)
            gather.write_as_yaml(
                [dataclasses.asdict(c) for c in comments], yaml_comments_path
            )

        log.info("Writing to an issue.yml per repository")
        gather.write_files()

    _dump_labels()
    _dump_task_tracer()

    log.info("Done converting manifest tasks to Gitea issues")


def pt_convert_differential(phab: Phabricator) -> None:
    for drev_file in sorted(common.orig_dirs["drev"].glob("**/*.json")):
        print("Processing %s..." % drev_file, end="")
        drev = common.readJsonFile(drev_file)
        print("loaded...", end="")

        converted = drevConvertToGitea(phab, drev)
        print("converted...", end="")
        drev_id = int(drev["id"])
        common.saveYamlFile(converted, pull_requests_dir / f"{drev_id:07}.yaml")
        print("saved...", end="")
        print("Done")


# These are stubs for now. Should be the 'main' inputs, providing guided choice of export/import process
def pt_convert_differential_transactions(phab: Phabricator) -> None:
    print("stub for now")


# Bare-bones convertor of 'task' data to a Gitea-struct; suitable for dumping to a YAML-file
def taskConvertToGitea(
    phab: Phabricator,
    input: dict[str, Any],
    ctx: heuristics.TaskGiteaContext,
) -> gt.Issue:
    fields = input["fields"]

    authorPhid = fields["authorPHID"]
    author = users.getBestEffortUser(phab, authorPhid)
    poster_id = author.gitea_userid
    poster_name = author.gitea_username

    # TODO: This is a hard-coded map of Phabricator status-types that mean 'closed'
    # Could be replaced by a dynamic lookup of a cached status-map via 'maniphest.status.search'
    # Also might involve using labels to map 'states'
    CLOSED_STATUSES = {"resolved", "invalid", "duplicate"}
    is_closed = fields["status"]["value"] in CLOSED_STATUSES

    date_closed = None
    if is_closed:
        orig_date_closed = fields.get("dateClosed")
        if orig_date_closed:
            date_closed = common.phabToGiteaTime(orig_date_closed)

    ownerPHID = fields["ownerPHID"]
    if ownerPHID:
        owner = users.getBestEffortUser(phab, ownerPHID)
        assignees = [owner.gitea_username]
    else:
        assignees = []

    subscriberPHIDs = (
        input.get("attachments", {}).get("subscribers", {}).get("subscriberPHIDs", [])
    )

    subscribers = []
    for subscriberPHID in subscriberPHIDs:
        # Some tasks are tagged with project subscriber.
        if not subscriberPHID.startswith("PHID-USER-"):
            continue
        subscriber_user = users.getBestEffortUser(phab, subscriberPHID)
        gitea_username = subscriber_user.gitea_username
        if gitea_username:
            subscribers.append(gitea_username)

    markup_context = markup_processor.Context(repository_name=ctx.repository)
    markdown_text = markup_processor.process_markup_to_markdown(
        markup_context, fields["description"]["raw"]
    )

    # Shorten title if necessary. It has a 255 character limit.
    title = fields["name"]
    if len(title) > 255:
        markdown_text = f"Original title: {title}\n\n" + markdown_text
        title = common.shorten_string(title)

    output = gt.Issue(
        number=input["id"],
        poster_id=poster_id,
        poster_name=poster_name,
        poster_email="",
        title=title,
        content=markdown_text,
        ref="",  # TODO: the Git branch that's referenced by this issue.
        milestone="",  # TODO
        state="closed" if is_closed else "open",
        is_locked=False,
        created=common.phabToGiteaTime(fields["dateCreated"]),
        updated=common.phabToGiteaTime(
            fields.get("dateModified", 0) or fields["dateCreated"]
        ),
        closed=date_closed,
        labels=labels_for_task(input, ctx),
        reactions=[],  # TODO
        assignees=assignees,
        subscribers=subscribers,
    )

    return output


# Handles converting 'differential' or 'drev' to Gitea 'pull-request' struct. suitable for dumping to yaml-file
def drevConvertToGitea(
    phab: Phabricator, input: dict[str, Any]
) -> list[dict[str, Any]]:
    author = users.getBestEffortUser(phab, input["fields"]["authorPHID"])

    output = {}
    output["number"] = input["id"]
    output["title"] = input["fields"]["title"][0:254]
    output["poster_id"] = author.gitea_userid
    output["poster_name"] = author.gitea_username
    output["poster_email"] = ""
    output["content"] = input["fields"]["summary"]  # TODO: strip newlines ?
    output["milestone"] = ""  # TODO
    output["created"] = common.phabToGiteaTime(int(input["fields"]["dateCreated"]))
    # Perhaps dateModified is always filled even if only just created. Hardcoding her in case it isnt
    if input["fields"]["dateModified"]:
        output["updated"] = common.phabToGiteaTime(int(input["fields"]["dateModified"]))
    else:
        output["updated"] = common.phabToGiteaTime(int(input["fields"]["dateCreated"]))

    # TODO: The logic below needs to be looked at carefully. See issue #8
    if input["fields"]["status"]["closed"] == True:
        output["state"] = "closed"
    else:
        output["state"] = "open"
    match input["fields"]["status"]["value"]:
        case "abandoned":  # Expired/forgotten submission ?
            output["merged"] = False
            output["merged_time"] = None
            output["merged_commit_sha"] = ""  # TODO: find out how to create this
        case "accepted":  # Accepted, but not yet merged
            output["merged"] = False
            output["merged_time"] = None
            output["merged_commit_sha"] = ""
        case "changes-planned":  # TODO: needs to be looked at
            output["merged"] = False
            output["merged_time"] = None
            output["merged_commit_sha"] = ""
        case "draft":  # TODO: needs to be looked at
            output["merged"] = False
            output["merged_time"] = None
            output["merged_commit_sha"] = ""
        case "needs-review":  # Under review
            output["merged"] = False
            output["merged_time"] = None
            output["merged_commit_sha"] = ""  # TODO
        case "needs-revision":  # Revision/changes required
            output["merged"] = False
            output["merged_time"] = None
            output["merged_commit_sha"] = ""  # TODO
        case "published":  # Accepted AND merged
            output["merged"] = True
            output["merged_time"] = common.phabToGiteaTime(
                int(input["fields"]["dateModified"])
            )  # TODO: almost certain to be WRONG... Needs transaction data most likely.
            output["merged_commit_sha"] = ""  # TODO
        case _:
            # do nothing; TODO: this should become an error when all existing/expected types have a convertor!
            pass

    head = {
        "clone_url": "",  # our own repo
        "ref": "",  # TODO: needs looking at
        "sha": "",  # TODO: can we even calculate this ?
        "repo_name": "blender",  # Our repo
        "owner_name": "blender-foundation",  # Us
    }
    base = {
        "clone_url": "",  # Always..
        "ref": "master",  # TODO: assuming we dont switch to MAIN ?
        "sha": "",  # TODO: needs calculating
        "repo_name": "blender",  # Our repo
        "owner_name": "blender-foundation",  # Us
    }
    output["head"] = head
    output["base"] = base
    output["assignees"] = []  # TODO
    output["is_locked"] = False  # TODO: assuming we do NOT have private tickets
    output["reactions"] = []  # TODO: might come from Transactions ?

    return [output]


def labels_for_task(
    phab_task: dict[str, Any],
    ctx: heuristics.TaskGiteaContext,
) -> list[gt.Label]:
    """Return labels for this Phabricator task.

    Because Gitea will only use the label name when importing issues, that's the
    only thing that'll be set for the returned labels. Their colors &
    descriptions will be stored in `org/repo/label.yml`.
    """
    label_names = ctx.labels.copy()

    # Convert subtype to label:
    subtype = phab_task["fields"].get("subtype")
    label_name = labels_for_task_subtype.get(subtype)
    if label_name:
        label_names.add(label_name)

    # Convert status to label:
    status_name = phab_task["fields"].get("status", {}).get("name")
    if status_name:
        label_names.add(f"Status::{status_name}")

    # Convert priority to label:
    priority_name = phab_task["fields"].get("priority", {}).get("name")
    if priority_name:
        label_names.add(f"Priority::{priority_name}")

    # Remember that we've used these labels.
    label_gatherer.remember(ctx.repository, label_names)

    return [gt.Label(name=name) for name in label_names]


def _dump_labels():
    log.info("Writing labels to YAML")
    for repo_name, labels in label_gatherer.items():
        yaml_path = paths.for_labels_yaml(repo_name)
        yaml_labels = [dataclasses.asdict(l) for l in labels]

        log.debug("Writing labels to %s", yaml_path)
        common.saveYamlFile(yaml_labels, yaml_path)


def _dump_task_tracer() -> None:
    yaml_path = paths.convert_dir / "tasks-to-org-repos.yml"
    log.info("Writing task traces to %s", yaml_path)
    common.saveYamlFile(task_tracer, yaml_path)


def _ensure_comment_timestamp(
    phab_task: dict[str, Any],
    comments: list[gt.Comment],
) -> None:
    """Replace epoch timestamps of comments with the task creation timestamp."""

    task_creation = common.phabToGiteaTime(phab_task["fields"]["dateCreated"])
    for comment in comments:
        comment.created = max(task_creation, comment.created)
        comment.updated = max(task_creation, comment.updated)
