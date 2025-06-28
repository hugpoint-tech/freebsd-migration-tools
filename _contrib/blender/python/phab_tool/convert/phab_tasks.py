import functools
from pathlib import Path
from typing import Any

from .. import common


@functools.cache
def load(jsonpath: Path) -> dict[str, Any]:
    """Load the given task from disk.

    Cached, so the task is only loaded once.
    """

    return common.readJsonFile(jsonpath)
