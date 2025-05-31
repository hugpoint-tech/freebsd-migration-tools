from typing import Any, Optional, Callable
import logging
import os

from phabricator import Phabricator

from .. import common, users
from . import gitea_types as gt
from . import user_mapping
from . import markup_processor
from . import heuristics, orgs_and_repos

_log = logging.getLogger(__name__)


def convertToGitea(
    phab: Phabricator,
    input_transactions: Any,
    issue_id: int,
    ctx: heuristics.TaskGiteaContext,
) -> list[gt.Comment]:
    """Handles converting 'transactions' to gitea.

    Note that transactions are comments, status-changes, etc.
    """
    gitea_comments: list[gt.Comment] = []

    # Order transactions by ID to get them in chronological order regardless of
    # their timestamp. This helps when generating multiple Gitea comments from a
    # single Phab transaction.
    input_transactions.sort(key=lambda t: t["id"])

    for transaction in input_transactions:
        # TODO: figure out other transaction-types
        # TODO: how to convert 'STATUS' changes. Import-format doesnt support these (?)
        # Transaction-types known: 'comment','create','description','mergedfrom','mergedinto','owner','priority',
        # 'projects','status','subscribers','subtype','title' and 'null'. The last type seems an internal thing without
        # ever providing externally useful info.
        match transaction["type"]:
            case "comment":
                comment = convertToGiteaComment(phab, transaction, issue_id, ctx)
                gitea_comments.append(comment)
            case "owner":
                comments = convertToGiteaAssignment(phab, transaction, issue_id)
                gitea_comments.extend(comments)
            case "status":
                comments = convertToGiteaStatus(phab, transaction, issue_id)
                gitea_comments.extend(comments)
            case "subscribers":
                comment = convertToGiteaSubscribers(phab, transaction, issue_id)
                gitea_comments.append(comment)
            case "title":
                maybe_comment = convertToGiteaTitle(phab, transaction, issue_id)
                if maybe_comment:
                    gitea_comments.append(maybe_comment)
            case "mergedinto":
                comments = convertToGiteaMergedInto(phab, transaction, issue_id, ctx)
                gitea_comments.extend(comments)
            case None:
                pass
            case _:
                # do nothing; TODO: this should become an error when all existing/expected types have a convertor
                _log.debug(
                    "Task T%d has unknown transaction type %s",
                    issue_id,
                    transaction["type"],
                )

    return gitea_comments


def convert_edges(
    phab: Phabricator,
    phab_edges: list[dict[str, Any]],
    issue_id: int,
    ctx: heuristics.TaskGiteaContext,
) -> list[gt.Comment]:
    """Convert Phabricator "edges" to Gitea comments."""
    gitea_comments: list[gt.Comment] = []

    # Mapping from edge type to converter for that type:
    edge_converters: dict[str, Callable[..., Optional[gt.Comment]]] = {
        "task.commit": _convert_edge_task_commit,
        "task.merged-in": _convert_edge_task_mergedin,
    }

    for edge_dict in phab_edges:
        converter = edge_converters.get(edge_dict["edgeType"])
        if not converter:
            continue
        comment = converter(phab, issue_id, ctx, edge_dict)
        if comment:
            gitea_comments.append(comment)

    return gitea_comments


def _task_transaction_to_comment(
    phab: Phabricator, transaction: dict[str, Any], issue_id: int
) -> gt.Comment:
    """Fills out the comment as well as possible with generic fields.

    The caller is responsible for filling out the content.
    """

    authorPhid = transaction["authorPHID"]
    if authorPhid.startswith("PHID-USER-"):
        author = users.getBestEffortUser(phab, authorPhid)
        poster_id = author.gitea_userid
        poster_name = author.gitea_username
    else:
        # PHID-RIDT-7ujdzga7zqtya6uu4v2p
        _log.debug(
            "Transaction %s of type %s on task T%d is authored by non-user %s",
            transaction["phid"],
            transaction["type"],
            issue_id,
            authorPhid,
        )
        poster_id = 0
        poster_name = ""

    comment = gt.Comment(
        issue_index=issue_id,
        poster_id=poster_id,
        poster_name=poster_name,
        poster_email="",
        created=common.phabToGiteaTime(transaction["dateCreated"]),
        updated=common.phabToGiteaTime(transaction["dateModified"]),
        content="",
    )
    return comment


# Specifific handler for converting comments to Gitea
def convertToGiteaComment(
    phab: Phabricator,
    transaction: dict[str, Any],
    issue_id: int,
    ctx: heuristics.TaskGiteaContext,
) -> gt.Comment:
    """Convert Phab comment to Gitea comment."""
    comment = _task_transaction_to_comment(phab, transaction, issue_id)
    comment.comment_type = gt.CommentType.comment

    content = _commentFindLatestContent(transaction["comments"])
    if content is None:
        content = f"*This comment was removed by @{comment.poster_name}*"

    markup_context = markup_processor.Context(repository_name=ctx.repository)
    comment.content = markup_processor.process_markup_to_markdown(
        markup_context,
        _sanitizeString(content),
    )

    return comment


def convertToGiteaAssignment(
    phab: Phabricator, transaction: dict[str, Any], issue_id: int
) -> list[gt.Comment]:
    """Convert Phab assignment change to Gitea comment.

    Gitea does not have support for importing these changes natively, so we have
    no other choice but to either discard or turn these into a comment.
    """

    # Gitea doesn't seem to do straight assignment from user A to B. Instead,
    # they add A and remove B, and those are two separate comments.

    comments = []

    def create(gitea_userid: int) -> gt.Comment:
        comment = _task_transaction_to_comment(phab, transaction, issue_id)
        comment.comment_type = gt.CommentType.assignees
        comment.meta["AssigneeID"] = gitea_userid
        comments.append(comment)
        return comment

    old_user_phid = transaction["fields"]["old"]
    if old_user_phid:
        old_user = users.getBestEffortUser(phab, old_user_phid)
        comment = create(old_user.gitea_userid)
        comment.meta["RemovedAssigneeID"] = True

    new_user_phid = transaction["fields"]["new"]
    if new_user_phid:
        new_user = users.getBestEffortUser(phab, new_user_phid)
        comment = create(new_user.gitea_userid)

    return comments


_is_open_status = {
    # Unknown-to-Phabricator status, translates to None in the Conduit API.
    # Just treat it as 'open'.
    None: True,
    "archived": False,
    "confirmed": True,
    "duplicate": False,
    "invalid": False,
    "needsdevelopertoreproduce": True,
    "needstriage": True,
    "needsuserinfo": True,
    "open": True,
    "resolved": False,
}

_status_names = {
    None: "Unknown Status",
    "archived": "Archived",
    "confirmed": "Confirmed",
    "duplicate": "Duplicate",
    "invalid": "Archived",  # 'invalid' was made friendlier as 'Archived'.
    "needsdevelopertoreproduce": "Needs Developer To Reproduce",
    "needstriage": "Needs Triage",
    "needsuserinfo": "Needs User Info",
    "open": "Open",
    "resolved": "Resolved",
}

# For now, this handler returns a 'comment' syntax. TODO: find out how to provide a gitea 'status' type
def convertToGiteaStatus(
    phab: Phabricator, transaction: dict[str, Any], issue_id: int
) -> list[gt.Comment]:
    """Convert Phab transaction to Gitea comment.

    Gitea cannot import actual status change history, so it's either comments or nothing.
    """
    comments: list[gt.Comment] = []
    comment = _task_transaction_to_comment(phab, transaction, issue_id)

    old_status = transaction["fields"]["old"]
    old_text = f" from {_status_names[old_status]!r}" if old_status else ""
    new_status = transaction["fields"]["new"]
    comment.content = f"Changed status{old_text} to: {_status_names[new_status]!r}"
    comments.append(comment)

    # Create 'close' or 'reopen' comment types.
    was_open = _is_open_status[old_status]
    is_open = _is_open_status[new_status]

    if not is_open and was_open:
        comment = _task_transaction_to_comment(phab, transaction, issue_id)
        comment.comment_type = gt.CommentType.close
        comments.append(comment)

    if is_open and not was_open:
        comment = _task_transaction_to_comment(phab, transaction, issue_id)
        comment.comment_type = gt.CommentType.reopen
        comments.append(comment)

    return comments


# TODO: Gitea import-logic does not provide for a 'subscriber' ? Currently done as comment
# NOTE: Phabricator provides a way to subscribe multiple people in one transaction. We produce one comment
def convertToGiteaSubscribers(
    phab: Phabricator, transaction: dict[str, Any], issue_id: int
) -> gt.Comment:
    added = []
    removed = []

    for operation in transaction["fields"]["operations"]:
        if not operation["phid"].startswith("PHID-USER-"):
            # Skip project subscribers and other non-users.
            continue
        user = users.getBestEffortUser(phab, operation["phid"])
        match operation["operation"]:
            case "add":
                added.append(user.gitea_username or "<unknown>")
            case "remove":
                removed.append(user.gitea_username or "<unknown>")
            case _:
                pass

    lines = []
    if added:
        added_nicks = ", ".join(f"@{nick}" for nick in added)
        s = "s" if len(added) > 1 else ""
        lines.append(f"Added subscriber{s}: {added_nicks}")
    if removed:
        s = "s" if len(removed) > 1 else ""
        removed_nicks = ", ".join(f"@{nick}" for nick in removed)
        lines.append(f"Removed subscriber{s}: {removed_nicks}")

    comment = _task_transaction_to_comment(phab, transaction, issue_id)
    comment.content = "\n".join(lines)

    return comment


def convertToGiteaTitle(
    phab: Phabricator, transaction: dict[str, Any], issue_id: int
) -> Optional[gt.Comment]:
    if not transaction["fields"]["old"]:
        # Phabricator seems to always has a "title" transaction, but a change
        # should only be recorded when we have an "old" title as well.
        return None

    comment = _task_transaction_to_comment(phab, transaction, issue_id)
    comment.comment_type = gt.CommentType.change_title
    comment.meta = {
        "NewTitle": common.shorten_string(transaction["fields"]["new"]),
        "OldTitle": common.shorten_string(transaction["fields"]["old"]),
    }
    return comment


def convertToGiteaMergedInto(
    phab: Phabricator,
    transaction: dict[str, Any],
    issue_id: int,
    ctx: heuristics.TaskGiteaContext,
) -> list[gt.Comment]:
    merged_to_task_phid = transaction["fields"].get("new")
    if not merged_to_task_phid:
        # Phabricator seems to produce two "mergedinto" transactions for a
        # merge. One has a list of "operations" that "add" the task PHID, and
        # the other just has an "old" and a "new" task PHID.
        #
        # This function just uses the simplest of the two: the one with "old"
        # and "new".
        return []

    comment = _task_transaction_to_comment(phab, transaction, issue_id)
    # Actually gt.CommentType.issue_ref should be used, but there is no importer for that on the Gitea side yet...
    # comment.comment_type = gt.CommentType.issue_ref

    # Find task info about merged_to_task_phid.
    merged_to_ctx = heuristics.task_context_of_phid(merged_to_task_phid)
    if merged_to_ctx.repository == ctx.repository:
        ref = f"#{merged_to_ctx.number}"
    else:
        ref = f"{merged_to_ctx.owner_repo}#{merged_to_ctx.number}"

    comment.content = f"Closed as duplicate of {ref}"

    # Add 2nd comment that indicates the comment was closed.
    comment_closed = _task_transaction_to_comment(phab, transaction, issue_id)
    comment_closed.comment_type = gt.CommentType.close

    return [comment, comment_closed]


# sanitizeString is used to catch any weird data that might be in phabricator
# Known issues are spurious nul-chars (/0's) in comments (see T97676) and possibly badly
# encoded emoji's. Standard emoji's seem to work well.
# Other stuff could be to filter all the \n's that got put into the comments, too.
def _sanitizeString(string: str) -> str:
    # For now, we stick to stripping NUL chars.
    return string.replace("\x00", "")


def _commentFindLatestContent(comments: list[dict[str, Any]]) -> Optional[str]:
    """Find the last version of the comment.

    :param comments: list of this comment's history.

    :returns: the content of the comment, or `None` if the comment was deleted.
    """

    latest = max(comments, key=lambda c: c["dateCreated"])
    if latest.get("removed"):
        return None
    return latest["content"]["raw"]


def _convert_edge_task_commit(
    phab: Phabricator,
    issue_id: int,
    ctx: heuristics.TaskGiteaContext,
    edge_dict: dict[str, Any],
) -> Optional[gt.Comment]:

    if "commit" not in edge_dict:
        return None

    fields = edge_dict["commit"]["fields"]
    repo_phid: str = fields["repositoryPHID"]
    gitea_repo_id = orgs_and_repos.repo_phid_to_gitea.get(repo_phid)

    commit_hash: str = fields["identifier"]
    phab_timestamp: Optional[int] = fields["author"]["epoch"]
    if phab_timestamp is None:
        phab_timestamp = fields["committer"]["epoch"]
    if phab_timestamp is None:
        raise RuntimeError(f"Commit {fields} in edge of task {issue_id} has None epoch")

    if gitea_repo_id and ctx.repository == gitea_repo_id.split("/", 1)[-1]:
        # Same repository, so just use the commit hash.
        commit_ref = commit_hash
    else:
        # Other repository, qualify it with the "org/repo".
        # NOTE: this has a bug (in the rendering, so importing this data is ok),
        # see https://github.com/go-gitea/gitea/issues/22666
        commit_ref = f"{gitea_repo_id}@{commit_hash}"
        _log.debug(
            "Found external ref from issue %d on %s to %s / %s",
            issue_id,
            ctx.repository,
            gitea_repo_id,
            commit_hash,
        )

    comment = gt.Comment(
        issue_index=issue_id,
        poster_id=0,
        poster_name="",
        poster_email="",
        created=common.phabToGiteaTime(phab_timestamp),
        updated=common.phabToGiteaTime(phab_timestamp),
        content=f"This issue was referenced by {commit_ref}",
    )

    return comment


def _convert_edge_task_mergedin(
    phab: Phabricator,
    issue_id: int,
    ctx: heuristics.TaskGiteaContext,
    edge_dict: dict[str, Any],
) -> Optional[gt.Comment]:
    # { "sourcePHID": "PHID-TASK-h3duz57xlqsnlqzkw3rg",
    #   "edgeType": "task.merged-in",
    #   "destinationPHID": "PHID-TASK-m72mvyjzp3gybulvje6r" }

    other_task_phid = edge_dict["destinationPHID"]
    other_task_ctx = heuristics.task_context_of_phid(other_task_phid)

    if ctx.repository == other_task_ctx.repository:
        # Same repository, so just use the issue ID.
        issue_ref = f"#{other_task_ctx.number}"
    else:
        # Other repository, qualify it with the "org/repo".
        # NOTE: this has a bug (in the rendering, so importing this data is ok),
        # see https://github.com/go-gitea/gitea/issues/22666
        issue_ref = f"{other_task_ctx.owner_repo}#{other_task_ctx.number}"

    comment = gt.Comment(
        issue_index=issue_id,
        poster_id=0,
        poster_name="",
        poster_email="",
        created=common.phabToGiteaTime(0),  # TODO: add a useful timestamp here.
        updated=common.phabToGiteaTime(0),  # TODO: add a useful timestamp here.
        content=f"{issue_ref} was marked as duplicate of this issue",
    )

    return comment
