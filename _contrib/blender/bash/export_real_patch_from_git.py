#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse
import dataclasses
import enum
import json
import logging
import multiprocessing
import subprocess
import time


GIT_REPO = Path("/data/blender")
PATCH_OUTPUT_PATH = Path("/data/patches")

MY_DIR = Path(__file__).absolute().parent
PHID_CMIT_PATH = MY_DIR.parent.parent / "migration-data/commits"


class Result(enum.Enum):
    OK = 1
    FAILED = 2
    SKIPPED = 3

    def add_to(self, progress: "Progress") -> None:
        match self:
            case self.OK:
                progress.num_commits_ok += 1
            case self.FAILED:
                progress.num_commits_failed += 1
            case self.SKIPPED:
                progress.num_commits_skipped += 1


@dataclasses.dataclass
class RepoResult:
    result: Result
    repoPrefix: str

    def add_to(self, per_repo_progress: dict[str, "Progress"]) -> None:
        self.result.add_to(per_repo_progress[self.repoPrefix])


@dataclasses.dataclass
class Progress:
    num_commits_ok: int = 0
    num_commits_failed: int = 0
    num_commits_skipped: int = 0

    def num_commits(self) -> int:
        return self.num_commits_ok + self.num_commits_failed + self.num_commits_skipped

    def __str__(self) -> str:
        return f"OK: {self.num_commits_ok:5}  FAIL: {self.num_commits_failed:5}  SKIP: {self.num_commits_skipped:5}"


log = logging.getLogger("patch_from_git")


def generate_patch(cmit_path: Path) -> RepoResult:
    with cmit_path.open("r") as infile:
        # cmit_data = {
        #     "phid": "PHID-CMIT-32f5ojesnxmz2egxpceu",
        #     "uri": "https://developer.blender.org/rB3384bb2c663fda4e8b2f63f37ffce7152436f0a5",
        #     "typeName": "Diffusion Commit",
        #     "type": "CMIT",
        #     "name": "rB3384bb2c663f",
        #     "fullName": "rB3384bb2c663f: RNA: add option to enable by default lib overridale flag of defined properties.",
        #     "status": "open"
        # }
        cmit_data = json.load(infile)
    uri: str = cmit_data["uri"]

    # Check that this is a Blender commit.
    try:
        prefix, git_hash = parse_phab_git_commit(uri)
    except ValueError:
        print(f"skipping non-git commit {uri}")
        return RepoResult(Result.SKIPPED, "unknown")

    if prefix != "rB":
        print(f"skipping non-Blender commit {prefix}{git_hash}")
        return RepoResult(Result.SKIPPED, prefix)

    patch_path = PATCH_OUTPUT_PATH / f"{cmit_path.stem}.patch"
    # print(f"writing to {patch_path}")
    try:
        git_into_file("format-patch", "-1", git_hash, "--stdout", into=patch_path)
    except subprocess.CalledProcessError as ex:
        log.error(
            "error processing commit %s:\n    cmd = %s\n    stderr = %s",
            git_hash,
            " ".join(ex.cmd),
            ex.stderr.replace("\n", "\n             "),
        )
        return RepoResult(Result.FAILED, prefix)
    return RepoResult(Result.OK, prefix)


def parse_phab_git_commit(url: str) -> tuple[str, str]:
    """Return (repo prefix, git hash).

    Raise ValueError if this is not a Git commit.

    >>> parse_phab_git_commit('https://developer.blender.org/rB3384bb2c663fda4e8b2f63f37ffce7152436f0a5')
    ('rB', '3384bb2c663fda4e8b2f63f37ffce7152436f0a5')
    >>> parse_phab_git_commit('https://developer.blender.org/rBAST3384bb2c663fda4e8b2f63f37ffce7152436f0a5')
    ('rBAST', '3384bb2c663fda4e8b2f63f37ffce7152436f0a5')
    >>> parse_phab_git_commit('https://developer.blender.org/M47')
    Traceback (most recent call last):
    ...
    ValueError: 'https://developer.blender.org/M47' is not a git hash URL
    """

    parsed = urlparse(url)
    commit_id = parsed.path
    if not commit_id:
        raise ValueError(f"{url!r} is not a git hash URL")

    # Hash is 40 chars, prefixed by '/r' + one or more letters.
    if len(commit_id) < 43:
        raise ValueError(f"{url!r} is not a git hash URL")

    return commit_id[1:-40], commit_id[-40:]


def git_into_file(*git_args: list[str], into=Path) -> None:
    with into.open("wb") as outfile:
        proc = subprocess.run(
            ["git", "-C", str(GIT_REPO), *git_args],
            encoding="utf-8",
            stdout=outfile,
            stderr=subprocess.PIPE,
            timeout=300,  # 5 minutes timeout
        )
    if proc.returncode != 0:
        # Remove the patch file on error.
        into.unlink(missing_ok=True)
        proc.check_returncode()


def main() -> None:
    # Sanity checks.
    if not PHID_CMIT_PATH.exists():
        raise SystemExit(f"{PHID_CMIT_PATH} does not exist")
    if not GIT_REPO.exists() or not (GIT_REPO / ".git").exists():
        raise SystemExit(f"Expecting Blender Git repository in {GIT_REPO}")
    PATCH_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    print(f"Going over all files in {PHID_CMIT_PATH}")

    start_time = time.monotonic()
    async_results = []
    progress: defaultdict[str, Progress] = defaultdict(Progress)

    try:
        with multiprocessing.Pool() as pool:
            # Queue up all the processes.
            for cmit_path in PHID_CMIT_PATH.glob("*.json"):
                # TODO: pass error_callback to process subprocess errors.
                async_res = pool.apply_async(generate_patch, (cmit_path,))
                async_results.append(async_res)

            # Handle the results
            for async_result in async_results:
                repo_res: RepoResult = async_result.get()
                repo_res.add_to(progress)

            pool.close()
            pool.join()
    except KeyboardInterrupt:
        print("Aborting on Ctrl+C")

    end_time = time.monotonic()

    print("Done!")
    num_commits = 0
    for prefix, prog in progress.items():
        print(f"{prefix:7}: {prog}")
        num_commits += prog.num_commits()

    duration = end_time - start_time
    print(f"Total time: {duration:.3} sec")
    print(f"            {1000 * duration / num_commits:.3} msec per commit")


if __name__ == "__main__":
    import doctest

    failure_count, _ = doctest.testmod()
    if failure_count:
        raise SystemExit("self-test failed")
    main()
