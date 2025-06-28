import dataclasses
import logging

from . import orgs_and_repos, paths
from .. import common

_log = logging.getLogger(__name__)


@dataclasses.dataclass
class TaskTracer:
    tasks_to_repo: dict[int, str] = dataclasses.field(default_factory=dict, init=False)
    """Mapping from task number to the Gitea `org/repo` it went into.

    This should make it possible to redirect from Phabricator task URLs to Gitea
    issue URLs.
    """

    def add(self, task_id: int, repo_name: str) -> None:

        repo = orgs_and_repos.repo_by_name(repo_name)
        org_repo = f"{repo.owner}/{repo.name}"

        try:
            existing_org_repo = self.tasks_to_repo[task_id]
        except KeyError:
            pass
        else:
            if existing_org_repo != org_repo:
                raise ValueError(
                    f"Task T{task_id} cannot go into both '{existing_org_repo}' and '{org_repo}'"
                )
            # Already in the dict, so we're done.
            return

        self.tasks_to_repo[task_id] = org_repo


@dataclasses.dataclass(frozen=True)
class UserIDTracer:
    phid_to_gitea_userid: dict[str, int]
    """Mapping from Phabricator PHID-USER-xxx to Gitea user ID."""

    def gitea_id(self, user_phid: str) -> int:
        """Get the Gitea user ID for this PHID.

        Raises a KeyError if this PHID is unknown.
        """
        if not user_phid.startswith("PHID-USER-"):
            raise ValueError(f"invalid user PHID: {user_phid!r}")
        return self.phid_to_gitea_userid[user_phid]

    def add(self, user_phid: str, gitea_user_id: int) -> None:
        if not user_phid.startswith("PHID-USER-"):
            raise ValueError(f"invalid user PHID: {user_phid!r}")
        if gitea_user_id <= 0:
            raise ValueError(f"invalid gitea user ID: {gitea_user_id!r}")

        try:
            existing_id = self.phid_to_gitea_userid[user_phid]
        except KeyError:
            pass
        else:
            if existing_id != gitea_user_id:
                raise ValueError(
                    f"{user_phid} cannot have multiple Gitea user IDs: {existing_id} and {gitea_user_id}"
                )
            # Already in the dict, so we're done.
            return

        self.phid_to_gitea_userid[user_phid] = gitea_user_id

    @classmethod
    def load(cls) -> "UserIDTracer":
        json_path = paths.for_user_id_mapping()
        try:
            mapping = common.readJsonFile(json_path)
        except FileNotFoundError:
            _log.info("No %s file, starting user mapping from scratch", json_path)
            return cls({})

        assert isinstance(mapping, dict), f"expected dict, got {type(mapping)}"
        _log.info("Loaded %s user mappings from %s", len(mapping), json_path)
        return cls(mapping)

    def save(self) -> None:
        json_path = paths.for_user_id_mapping()
        _log.info(
            "Writing user map of %d users to %s",
            len(self.phid_to_gitea_userid),
            json_path,
        )
        common.saveJsonFile(self.phid_to_gitea_userid, json_path)
