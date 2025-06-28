from pathlib import Path
from typing import Optional

from . import heuristics, orgs_and_repos

convert_dir = Path("convert")


def for_org(organization_name: str) -> Path:
    return convert_dir / organization_name


def for_repo(
    organization_name: str,
    repo_name: str,
    *,
    root: Optional[Path] = None,
) -> Path:
    if root is None:
        root = convert_dir
    return root / organization_name / repo_name


def for_issues_yaml(ctx: heuristics.TaskGiteaContext) -> Path:
    repo = orgs_and_repos.repo_by_name(ctx.repository)
    return for_repo(repo.owner, repo.name) / "issue.yml"


def for_issue_comments_yaml(ctx: heuristics.TaskGiteaContext, task_id: int) -> Path:
    repo = orgs_and_repos.repo_by_name(ctx.repository)
    return for_repo(repo.owner, repo.name) / "comments" / f"{task_id}.yml"


def for_labels_yaml(repo_name: str) -> Path:
    repo = orgs_and_repos.repo_by_name(repo_name)
    return for_repo(repo.owner, repo.name) / "label.yml"


def for_user_id_mapping() -> Path:
    # If this changes, also update reset-gitea.sh, as it erases this file.
    return convert_dir / "user-ids.json"


def for_user_mapping() -> Path:
    # If this changes, also update reset-gitea.sh, as it erases this file.
    return convert_dir / "users.csv"


def for_blender_id_user_csv() -> Path:
    # This file does not have to be rsynced to the server and contains private
    # information, so keep it out of the "convert" directory.
    return Path("phab-users-for-blenderid.csv")
