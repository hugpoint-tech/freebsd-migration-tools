#!/usr/bin/env python

"""Import everthing from ./convert into Gitea.

- Run ./pt.convert first, to convert all the Phab data to Gitea data.
- Then run this file to actually do the import.
"""
import abc
import inspect
import logging
import os
import shlex
import socket
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

# Load settings from the .env file into os.environ.
load_dotenv()

from phab_tool import gitea, common
from phab_tool.convert import gitea_types as gt
from phab_tool.convert import orgs_and_repos, paths
from phab_tool.gitea_api.api import repository_api
import phab_tool.gitea_api.exceptions as api_exceptions

_log = logging.getLogger(__name__)


class CommandRunner(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def gitea_restore_repo(self, repo: gt.Repository) -> None:
        """Run `gitea restore-repo`"""

    @abc.abstractmethod
    def run_subprocess(self, cli_args: list[str]) -> None:
        """Run the CLI arguments."""

    @abc.abstractmethod
    def ensure_git_clone(self, repo: gt.Repository) -> None:
        """Ensure the 'git' directory exists and is up to date."""

    @abc.abstractmethod
    def __enter__(self) -> "CommandRunner":
        pass

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def main():
    if any("help" in arg for arg in sys.argv[1:]):
        print(f"Usage: {sys.argv[0]} [repo]")
        raise SystemExit()

    time_start = time.monotonic()
    repos_to_import: set[str] = set(sys.argv[1:])

    if repos_to_import:
        _log.info("Importing data into Gitea repositories: %s", repos_to_import)
    else:
        _log.info("Importing data into Gitea")

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)7s %(name)s %(message)s"
    )

    # Get the runner that can do the import.
    runner: CommandRunner
    env_var = os.environ.get("GITEA_USE_REMOTE", "")
    if env_var.lower() in {"true", "yes", "1"}:
        runner = ScriptWritingRunner()
    else:
        runner = RealCommandRunner()

    # This should have been done already by running `pt.convert`, but just run
    # it again for ease fo testing things.
    orgs_and_repos.create_repo_dirs_for_conversion()
    orgs_and_repos.ensure_orgs_on_gitea()

    with runner:
        for org_repos in orgs_and_repos.REPOS.values():
            for repo in org_repos:
                if repos_to_import and repo.name not in repos_to_import:
                    continue

                erase_existing_gitea_repo(repo)
                runner.ensure_git_clone(repo)
                runner.gitea_restore_repo(repo)

    duration = time.monotonic() - time_start
    _log.info(
        "Done importing data into Gitea, it took %s", common.humanize_duration(duration)
    )


def erase_existing_gitea_repo(repo: gt.Repository) -> None:
    """Erase the Gitea repository that we'll import into soon."""

    client = gitea.api_client()
    repoAPI = repository_api.RepositoryApi(client)
    try:
        repoAPI.repo_delete(repo.owner, repo.name)
    except api_exceptions.NotFoundException:
        pass
    else:
        _log.info("Erased Gitea repository %s/%s", repo.owner, repo.name)


class RealCommandRunner(CommandRunner):
    def gitea_restore_repo(self, repo: gt.Repository) -> None:
        """Run `gitea restore-repo`"""
        gitea = os.environ["GITEA_EXECUTABLE"]

        repo_path = paths.for_repo(repo.owner, repo.name)
        _log.info("Importing into Gitea: %s", repo_path)

        cli_args = [
            gitea,
            "restore-repo",
            "--validation",
            "-r",
            # Conversion to absolute path is necessary, otherwise the Gitea server
            # resolves it relative to its own CWD.
            str(repo_path.absolute()),
            "--owner_name",
            repo.owner,
            "--repo_name",
            repo.name,
        ]
        self.run_subprocess(cli_args)

    def run_subprocess(self, cli_args: list[str]) -> None:
        """Run the CLI arguments as subprocess."""
        proc = subprocess.run(
            cli_args,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=3600,  # 60 minutes timeout
        )
        if proc.returncode:
            raise RuntimeError(
                f"Error {proc.returncode} calling {' '.join(cli_args)}:\n{proc.stdout}"
            )

    def ensure_git_clone(self, repo: gt.Repository) -> None:
        """Ensure the 'git' directory exists and is up to date."""

        repo_path = paths.for_repo(repo.owner, repo.name)
        target_dir = repo_path / "git"

        if not repo.clone_url:
            _log.info("Repo '%s' has no Git repository, faking Git checkout", repo.name)
            if target_dir.exists():
                return
            git_cwd = target_dir.parent
            git_cliargs = ["init", "--bare", target_dir.name]
        elif target_dir.exists() and (target_dir / "HEAD").exists():
            _log.info("Fetching %s into %s", repo.clone_url, target_dir)
            git_cwd = target_dir
            git_cliargs = ["fetch", "--prune", "--prune-tags", "--force"]
        else:
            _log.info("Cloning %s into %s", repo.clone_url, target_dir)
            git_cwd = target_dir.parent
            git_cliargs = ["clone", "--mirror", repo.clone_url, target_dir.name]

        git_args = ["git", "-C", str(git_cwd)] + git_cliargs
        _log.debug("running %s", " ".join(git_args))
        self.run_subprocess(git_args)

    def __enter__(self) -> "CommandRunner":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class ScriptWritingRunner(CommandRunner):
    script_path = paths.convert_dir / "import-all.sh"

    def __init__(self) -> None:
        super().__init__()
        _log.info("Writing to shell script at %s", self.script_path)
        self._scriptfile = self.script_path.open("w", encoding="utf-8")
        self._write_script("### Auto-generated script to import Gitea projects")
        self._write_script(f"### Created on {datetime.now():%Y-%m-%d %H:%M:%S %Z}")
        self._write_script(f"### By {os.getlogin()}@{socket.gethostname()}")
        self._write_script("")
        self._write_script("set -e  # Break on errors")
        self._write_script("")

        self._remote_data_root = Path(os.environ["GITEA_REMOTE_DATA_PATH"])
        _log.info("Assuming the converted data will live at %s", self._remote_data_root)

        self._rsync_host = os.environ["GITEA_RSYNC_HOST"]
        self._remote_gitea_config = os.environ["GITEA_REMOTE_CONFIG_PATH"]

    def gitea_restore_repo(self, repo: gt.Repository) -> None:
        """Run `gitea restore-repo`"""
        gitea = os.environ["GITEA_REMOTE_EXECUTABLE"]

        repo_path = paths.for_repo(repo.owner, repo.name, root=self._remote_data_root)
        _log.info("Importing into Gitea: %s", repo_path)
        self._write_script(f'echo "Restoring info Gitea: {repo_path}"')

        cli_args = [
            gitea,
            "restore-repo",
            "-c",
            self._remote_gitea_config,
            "-r",
            # Conversion to absolute path is necessary, otherwise the Gitea server
            # resolves it relative to its own CWD.
            str(repo_path.absolute()),
            "--owner_name",
            repo.owner,
            "--repo_name",
            repo.name,
        ]
        self.run_subprocess(cli_args)

    def run_subprocess(self, cli_args: list[str]) -> None:
        """Run the CLI arguments as subprocess."""
        quoted = " ".join(shlex.quote(a) for a in cli_args)
        self._write_script(quoted)

    def ensure_git_clone(self, repo: gt.Repository) -> None:
        """Ensure the 'git' directory exists and is up to date."""

        repo_path = paths.for_repo(repo.owner, repo.name, root=self._remote_data_root)
        target_dir = repo_path / "git"

        if repo.clone_url:
            script = f"""
                # Ensure a fresh Git checkout lives at {target_dir}.
                if [ -d "{target_dir}" -a -e "{target_dir}/HEAD" ]; then
                    echo "Fetching {repo.clone_url} at {target_dir}"
                    git -C {target_dir} fetch --prune --prune-tags --force
                else
                    echo "Cloning {repo.clone_url} into {target_dir}"
                    git -C {target_dir.parent} clone --bare {repo.clone_url} {target_dir.name}
                fi
                """
        else:
            script = f"""
                # Ensure an empty Git repo lives at {target_dir} to appease Gitea.
                # This repository doesn't actually have a Git repo, but Gitea cannot live without.
                if [ ! -d "{target_dir}" ]; then
                    echo "Creating empty Git repo at {target_dir}"
                    git -C {target_dir.parent} init --bare {target_dir.name}
                fi
                """
        self._write_script(inspect.cleandoc(script))

    def _write_script(self, script: str) -> None:
        print(script, file=self._scriptfile)

    def __enter__(self) -> "CommandRunner":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._write_script("")
        self._write_script("echo Done importing into Gitea.")

        self._scriptfile.close()
        self.script_path.chmod(0o755)

        _log.info(
            "rsync with:\nrsync ./convert/ %s:%s/ --exclude git -a",
            self._rsync_host,
            self._remote_data_root,
        )
        _log.info(
            "and then run on the remote host:\n%s/%s",
            self._remote_data_root,
            self.script_path.name,
        )

        return False


if __name__ == "__main__":
    main()
