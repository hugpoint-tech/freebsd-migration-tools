import os
from dataclasses import dataclass, field
from typing import Any

"""Types that Gitea expects in its YAML files.

Gitea imports repository info from YAML files. Their layout is defined by
Gitea's Go code.

The core of the "repo restore" code lives in `services/migrations/restore.go`
and in the `migrateRepository()` function in `services/migrations/migrate.go`.
"""


@dataclass
class Issue:
    """Gitea issue.

    Gitea Source: modules/migration/issue.go
    """

    number: int
    poster_id: int
    poster_name: str
    poster_email: str
    title: str
    content: str
    ref: str  # Git branch/tag this issue references.
    milestone: str
    state: str  # closed, open
    is_locked: bool
    created: str  # ISO-8601 timestamp
    updated: str  # ISO-8601 timestamp
    closed: str | None  # ISO-8601 timestamp, optional
    labels: list["Label"]
    reactions: list["Reaction"]
    assignees: list[str]  # usernames
    subscribers: list[str]  # usernames


@dataclass(frozen=True)
class Label:
    """Gitea label.

    Gitea source: modules/migration/label.go
    """

    name: str

    # These two are only used from `org/repo/label.yml`. Labels mentioned in
    # Issues are identified by their name only.
    color: str = ""  # HTML hex code without leading #
    description: str = ""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Label):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Label):
            return False
        return self.name < other.name


@dataclass
class Reaction:
    """Gitea reaction.

    Gitea source: modules/migration/reaction.go
    """

    user_id: int
    user_name: str
    content: str


# See `commentStrings` in models/issues/comment.go
# There don't seem to be comment types for status changes (because in Gitea it's
# just "open" or "closed"), issue description changes, or for subscriber changes.
#
# See `func (g *GiteaLocalUploader) CreateComments(comments ...*base.Comment) error`
# in `services/migrations/gitea_uploader.go` for how they are imported.
class CommentType:
    assignees = "assignees"
    change_title = "change_title"
    close = "close"
    comment = "comment"
    comment_ref = "comment_ref"
    commit_ref = "commit_ref"
    issue_ref = "issue_ref"
    label = "label"
    reopen = "reopen"


@dataclass
class Comment:
    """Gitea comment.

    Gitea source: modules/migration/comment.go
    """

    issue_index: int
    poster_id: int
    poster_name: str
    poster_email: str
    created: str  # ISO-8601 timestamp
    updated: str  # ISO-8601 timestamp
    content: str

    # comment_type determines which fields are read from 'meta'.
    # See services/migrations/gitea_uploader.go, function
    # func (g *GiteaLocalUploader) CreateComments(comments ...*base.Comment) error
    comment_type: str = CommentType.comment
    meta: dict[str, Any] = field(default_factory=dict)

    # These are available, but don't need to be exported. Until we actually want
    # to populate them, leave them out.
    # index: int
    # reactions: list[Reaction] = None


@dataclass
class Repository:
    """Gitea repository.

    Gitea source: modules/migration/repo.go

    Some sensible defaults have been set.
    """

    name: str
    owner: str
    description: str

    is_private: bool = False
    is_mirror: bool = False
    clone_url: str = ""
    original_url: str = ""
    defaultbranch: str = "master"

    def construct_original_url(self) -> None:
        gitea = os.environ["GITEA_URL"]
        url = f"{gitea}/{self.owner}/{self.name}"
        self.original_url = url


@dataclass
class Project:
    """Gitea project.

    Gitea source: modules/migration/project.go
    """

    title: str
    description: str = ""
    type: str = "repository"  # individual, repository, or organization
