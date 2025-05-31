import logging
import dataclasses
from collections import defaultdict
from typing import Any, Optional
from types import EllipsisType

from . import projects, orgs_and_repos

_log = logging.getLogger(__name__)

# Strings that are searched for in the task description. These are only used if
# there are no known project tags what so ever on the task.
BLENDER_TAGLINES: set[str] = {
    "**Blender Version**",
}


@dataclasses.dataclass
class TaskGiteaContext:
    """For a Phabricator Task, the context where it should go in Gitea."""

    number: int
    """The task number on Gitea."""

    reject: bool = False
    """Reject this task."""

    repository: str = ""
    """Name of the Gitea repository. It's kinda unique now, so also identifies the org."""

    project: str = ""
    """Name of the Gitea project of that repo, corresponds to the module owning this issue."""

    labels: set[str] = dataclasses.field(default_factory=set)

    # board: str
    # """Name of the board inside that project, corresponds to Phabricator workboards."""

    # TODO maybe also add milestones here?
    # milestone: str

    @property
    def owner_repo(self) -> str:
        """Return the 'owner/repo' string for this task.

        Returns an empty string if the repository is not known.
        """
        if not self.repository:
            return ""
        repo = orgs_and_repos.repo_by_name(self.repository)
        return f"{repo.owner}/{repo.name}"


# Mapping from task PHID to its context.
_task_contexts: dict[str, TaskGiteaContext] = {}


def task_context(task: dict[str, Any]) -> TaskGiteaContext:
    """Heuristically guess which repository this Phabricator task should go into.

    Caches the context in _task_contexts, so that task_context_of_phid() can do
    its work.
    """

    task_phid = task["phid"]
    try:
        ctx = _task_contexts[task_phid]
    except KeyError:
        ctx = _task_context(task)
        _task_contexts[task_phid] = ctx
    return ctx


def task_context_of_phid(task_phid: str) -> TaskGiteaContext:
    """Return the TaskGiteaContext of this task.

    :raises: KeyError if the task PHID is unknown. Be sure to call
        task_context(task) before using this function to populate the cache.
    """
    if not task_phid.startswith("PHID-TASK-"):
        raise ValueError(f"Not a task PHID: {task_phid!r}")
    return _task_contexts[task_phid]


def _task_context(task: dict[str, Any]) -> TaskGiteaContext:
    """Heuristically guess which repository this Phabricator task should go into.

    This function doesn't cache anything in _task_contexts.
    """
    # _task_context_by_project_slugs() returns a ctx that also contains a few
    # labels, even when it turns out the project assignment cannot be used to
    # uniquely identify a repository.
    rich_ctx = _task_context_by_project_slugs(task)
    if rich_ctx.repository:
        return rich_ctx

    weaker_ctx = _task_context_by_description(task)
    if weaker_ctx:
        rich_ctx.repository = weaker_ctx.repository
        rich_ctx.reject = weaker_ctx.reject
        return rich_ctx

    weaker_ctx = _task_context_by_subtype(task)
    if weaker_ctx:
        rich_ctx.repository = weaker_ctx.repository
        rich_ctx.reject = weaker_ctx.reject
        return rich_ctx

    # This task can't be rejected, but can't be identified as Blender either.
    # It's still likely to be for Blender, so put it there & add a label that
    # indicates the uncertainty.
    rich_ctx.repository = "blender"
    rich_ctx.labels.add("migration/requires-manual-verification")
    return rich_ctx


def _task_context_by_project_slugs(task: dict[str, Any]) -> TaskGiteaContext:
    proj_slugs = projects.project_slugs(task)

    if projects.must_reject(proj_slugs):
        return TaskGiteaContext(task["id"], reject=True)

    # Count how often things were assigned. This can help to resolve ambiguity.
    nonblender: dict[str, int] = defaultdict(int)
    repo_names: dict[str, int] = defaultdict(int)
    gitea_projects: dict[str, int] = defaultdict(int)
    labels: set[str] = set()
    blender_modules: set[str] = set()

    for task_slug in proj_slugs:
        # Blender Modules:
        for module, sub_slugs in projects.module_projects.items():
            if task_slug == module or task_slug in sub_slugs:
                repo_names["blender"] += 1  # This is Blender
                gitea_projects[module] += 1
                blender_modules.add(module)
                # Uncomment to include the sub-module slugs:
                # blender_modules.update({task_slug} & set(sub_slugs))

        # Blender versions:
        if task_slug in projects.blender_milestones:
            repo_names["blender"] += 1

        # Must-be-Blender projects:
        if task_slug in projects.blender_slugs:
            repo_names["blender"] += 1

        # Single project-to-repo relations:
        if task_slug in projects.repositories:
            repo_name = projects.repositories[task_slug]
            nonblender[repo_name] += 1

        # Labels:
        if task_slug in projects.labels:
            label = projects.labels[task_slug]
            labels.add(label)

    labels.update(projects.labels[module] for module in blender_modules)

    # Also some migration metadata. We can remove those labels later when we feel there's no more need.
    labels.update(
        label
        for slug in sorted(proj_slugs)
        if (label := projects.label_for_project(slug))
    )

    ctx = TaskGiteaContext(task["id"], labels=labels)

    if nonblender:
        # In this case, `repo_names` doesn't matter. It likely contains
        # "blender" for plenty of tasks that shouldn't go into the Blender
        # repository (like documentation and other Blender-related projects, but
        # also for add-ons that are also tagged with a Blender module).
        ctx.repository = _most(nonblender)
        return ctx

    if repo_names:
        # This should just be Blender itself.
        ctx.repository = _most(repo_names)
        if ctx.repository != "blender":
            _log.warning(
                "Task T%d has non-Blender repository in 'repo_names': '%s'",
                task["id"],
                dict(repo_names),
            )
        module_label = projects.label_for_module(frozenset(blender_modules))
        if module_label:
            ctx.labels.add(module_label)
        return ctx

    # Nothing was found so far, fall back to weak relations.
    weak_repos = {
        repo for (slug, repo) in projects.weak_slugs.items() if slug in proj_slugs
    }
    if len(weak_repos) == 1:
        ctx.repository = weak_repos.pop()
        return ctx

    if weak_repos:
        _log.warning(
            "Task T%d has multiple weak repositories: %s", task["id"], weak_repos
        )
    return ctx


def _task_context_by_description(task: dict[str, Any]) -> Optional[TaskGiteaContext]:
    """Inspect the description to see if we can get somewhere.

    :return: The detected repository, or None if nothing was recognised.
    """

    description: str = task["fields"].get("description", {}).get("raw") or ""
    if not description.strip():
        _log.debug(
            "Task T%d has no project tags and no description, rejecting",
            task["id"],
        )
        return TaskGiteaContext(task["id"], reject=True)

    if any(tagline in description for tagline in BLENDER_TAGLINES):
        _log.debug(
            "Task T%d recognised Blender from the description",
            task["id"],
        )
        return TaskGiteaContext(task["id"], repository="blender")

    if "spam" in description.lower():
        _log.debug("Task T%d recognised as spam, rejecting", task["id"])
        return TaskGiteaContext(task["id"], reject=True)

    return None


def _task_context_by_subtype(task: dict[str, Any]) -> Optional[TaskGiteaContext]:
    """Inspect the subtype to see if we can get somewhere.

    :return: The detected repository, or None if nothing was recognised.
    """

    subtype: str = task["fields"].get("subtype") or ""
    if subtype and subtype != "default":
        # A non-default sub-type (so bug, todo, design, etc.). Likely to be
        # Blender, as others would have been recognised by their project tags.
        _log.debug(
            "Task T%d recognised Blender from its subtype",
            task["id"],
        )
        return TaskGiteaContext(task["id"], repository="blender")

    return None


def _most(counted_strings: dict[str, int], ambiguous: str | EllipsisType = ...) -> str:
    """Return the string with the highest count.

    :param counted_things: mapping from "string" to "count".
    :param ambiguous: if there are multiple most-counted strings, return the
        first one (...) or the value of this parameter (anything else).
    """
    if not counted_strings:
        return ""

    by_count = defaultdict(set)
    for thing, count in counted_strings.items():
        by_count[count].add(thing)

    assert len(by_count) > 0

    max_count = max(by_count.keys())
    most_counted: set[str] = by_count[max_count]
    if len(most_counted) == 1:
        return most_counted.pop()

    if ambiguous is ...:
        # Just grab one of them. Use sorting to make the result predictable (for tests).
        return sorted(most_counted)[0]

    return ambiguous
