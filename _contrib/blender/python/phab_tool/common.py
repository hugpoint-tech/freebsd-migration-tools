import dataclasses
import datetime
import json
import logging
import os
import re
import time
from pathlib import Path
from typing import Any, TypeVar, Sequence, Iterable

import yaml

# Dir with original Phabricator data.
orig_dir = Path("data/orig")

orig_dirs = {
    "task": orig_dir / "task",
    "xact-task": orig_dir / "xact-task",
    "edge-task": orig_dir / "edge-task",
    "drev": orig_dir / "drev",
    "bake": orig_dir / "bake",
    "diff": orig_dir / "diff",
    "xact-diff": orig_dir / "xact-diff",
    "xact-drev": orig_dir / "xact-drev",
    "user": orig_dir / "user",
    "file": orig_dir / "file",
    "file_data": orig_dir / "file_data",
    "paste": orig_dir / "paste",
    "user-email": orig_dir / "phabricator-user_email",
    "blender-id": orig_dir / "blender_id-users",
    "repo": orig_dir / "repo",
}


# Configure the YAML writer to always quote strings:
def _quoted_presenter(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')


yaml.add_representer(str, _quoted_presenter)


def subpath(identifier: int, suffix: str = "") -> Path:
    """
    >>> subpath(123456, '.txt').as_posix()
    '0123/0123456.txt'
    >>> subpath(123456).as_posix()
    '0123/0123456'
    """
    assert isinstance(identifier, int), f"expected int, not {identifier!r}"
    subpath = f"{identifier:07}"
    return Path(subpath[:-3]) / (subpath + suffix)


def saveYamlFile(data: Any, filename: str | Path) -> None:
    """Saves a Yaml-formatted file representing 'data' on location 'filename'"""

    if isinstance(filename, str):
        filename = Path(filename)
    filename.parent.mkdir(exist_ok=True, parents=True)

    if dataclasses.is_dataclass(data):
        data = dataclasses.asdict(data)

    with open(filename, "w") as f:
        yaml.dump(data, f)


def asYAML(data: Any) -> str:
    """Converts the data to YAML."""

    if dataclasses.is_dataclass(data):
        data = dataclasses.asdict(data)

    contents: str = yaml.dump(data)
    return contents


def saveTextFile(contents: str, filename: str | Path) -> None:
    """Saves a text file on location 'filename'"""

    if isinstance(filename, str):
        filename = Path(filename)
    filename.parent.mkdir(exist_ok=True, parents=True)
    filename.write_text(contents)


def saveJsonFile(data: Any, filename: str | Path) -> None:
    """Saves a JSON-formatted file representing 'data' on location 'filename'"""

    if isinstance(filename, str):
        filename = Path(filename)
    filename.parent.mkdir(exist_ok=True, parents=True)

    if dataclasses.is_dataclass(data):
        data = dataclasses.asdict(data)

    # Create a backup of the file before overwriting it.
    bak_name = filename.with_suffix(filename.suffix + "~")
    if filename.exists():
        bak_name.unlink(missing_ok=True)
        filename.rename(bak_name)

    with open(filename, "w") as f:
        json.dump(data, f, indent="  ")

    # Only erase the backup if the dump was OK.
    bak_name.unlink(missing_ok=True)


def readJsonFile(file: str | Path) -> Any:
    """Returns struct represented by JSON in 'file'"""
    with open(file, "r") as f:
        data = json.load(f)
    return data


def needs_processing(input_file: Path, output_file: Path) -> bool:
    """Answers "does this input file needs to be processed?" based on timestamps.

    If 'input_file' does not exist, raises FileNotFoundError.
    If 'output_file' does not exist, always returns True.
    """

    try:
        mtime_out = output_file.stat().st_mtime
    except FileNotFoundError:
        # No output file, so input needs to be processed.
        return True

    mtime_in = input_file.stat().st_mtime
    return mtime_out < mtime_in


def shorten_string(value: str, length: int = 255) -> str:
    """Shorten the string to max `length` characters.

    >>> shorten_string("abcdefg", 4)
    'a...'
    >>> shorten_string("abcdefg", 6)
    'abc...'
    >>> shorten_string("abcdefg", 7)
    'abcdefg'
    >>> shorten_string("abcdefg", 255)
    'abcdefg'
    """
    if len(value) <= length:
        return value

    return value[0 : length - 3] + "..."


def humanize_duration(seconds: float) -> str:
    humanized = ""
    if (seconds / 86400) >= 1:
        day = int(seconds / 86400)
        seconds = seconds - 86400 * day
        humanized = f"{day}d "
    if (seconds / 3600) >= 1:
        hour = int(seconds / 3600)
        seconds = seconds - 3600 * hour
        humanized = humanized + f"{hour}h "
    if (seconds / 60) >= 1:
        minutes = int(seconds / 60)
        seconds = seconds - 60 * minutes
        humanized = humanized + f"{minutes}m "
    humanized = humanized + f"{seconds:.0f}s"
    return humanized


def humanize_timestamp(timestamp: int) -> str:
    """Humanize a Phabricator timestamp.

    :param timestamp: UNIX timestamp in the UTC timezone.
    """

    dt = parse_timestamp(timestamp)
    return dt.strftime("%Y-%m-%d %H:%M:%S %Z")


def parse_timestamp(timestamp: int) -> datetime.datetime:
    """Parse a Phabricator timestamp.

    :param timestamp: UNIX timestamp in the UTC timezone.
    """
    return datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)


def phabToGiteaTime(phab_timestamp: int) -> str:
    """Convert Phabricator to Gitea time.

    Convert time from UTC UNIX timestamp to ISO-8601 format.
    """
    dt = datetime.datetime.utcfromtimestamp(phab_timestamp)
    return dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")


T = TypeVar("T")


def timed_iter(
    log: logging.Logger, items: Sequence[T], num_items: int | None = None
) -> Iterable[T]:
    if num_items is None:
        num_items = len(items)

    # Gather some more iterations before attempting any guess at "time left".
    # Since this can be used from parallelizable code, use 3*CPU-count
    # to make sure the workers are saturated.
    cpu_count = os.cpu_count()
    assert cpu_count is not None
    num_items_before_time_guess = cpu_count * 3

    time_start = time.monotonic()
    time_last_log = -float("inf")

    for idx, item in enumerate(items):
        time_now = time.monotonic()
        if time_now - time_last_log < 1:
            # Log no more than one entry per second.
            yield item
            continue
        time_last_log = time_now

        time_duration = time_now - time_start

        if idx < num_items_before_time_guess and time_duration < 10:
            log.info("Processing %d of %d", idx, num_items)
            yield item
            continue

        time_total_expect = (time_duration / idx) * num_items
        time_left = time_total_expect - time_duration

        log.info(
            "Processing %d of %d  %s left",
            idx,
            num_items,
            humanize_duration(time_left),
        )
        yield item


# NOTE: When modified ensure the corresponding function in the PHP baking code is
# also updated (MakeFilemameSafe).
def make_file_name_safe(file_name: str) -> str:
    return re.sub(r"[^\w\-_\.]", "_", file_name)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
