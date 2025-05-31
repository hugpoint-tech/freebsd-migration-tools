from collections import defaultdict
from pathlib import Path
from typing import Any, TypeAlias
import functools
import logging
import multiprocessing
import multiprocessing.pool
import os
import signal

from . import common


MULTIPROCESSING_TIMEOUT = 3600 * 10  # seconds


class Pool(multiprocessing.pool.Pool):
    """Multiprocessing pool that behaves on Ctrl+C."""

    def __init__(
        self,
        processes=None,
        initializer=None,
        initargs=(),
        maxtasksperchild=None,
        context=None,
    ):
        # Ensure that the child processes don't handle SIGINT themselves.
        original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
        try:
            super().__init__(
                processes, initializer, initargs, maxtasksperchild, context
            )
        finally:
            signal.signal(signal.SIGINT, original_sigint_handler)


StringPromise: TypeAlias = multiprocessing.pool.AsyncResult[str]


class OutputGatherer:
    """Context manager for parallel YAML conversion.

    Parallel conversion of data to YAML.

    - Joining into one file: use `append(data)`. The joined output can be
      obtained with `combined_output()` or directly written to disk with
      `write_combined(path)`.
    - Writing individual files: use `write_as_yaml(data, filepath)`.
    """

    def __init__(self, log: logging.Logger) -> None:
        self._chunks: list[str] = []
        self._yaml_promises: list[StringPromise] = []
        self._file_promises: dict[Path, list[StringPromise]] = defaultdict(list)

        num_workers = os.cpu_count()
        self._pool = Pool(num_workers)

        self._log = log
        self._log.info("Using %d CPUs for parallel processing", num_workers)

    def append(self, data: Any) -> None:
        """Queue the conversion of this data to a chunk of YAML.

        AFTER the pool is closed, call write_combined(path) to write the data to disk.
        """
        promise = self._pool.apply_async(common.asYAML, (data,))
        self._yaml_promises.append(promise)

    def append_as_yaml(self, data: Any, yamlpath: Path) -> None:
        """Convert data to YAML and append to a specific file.

        The appending to file only happens when write_files() is
        called. That should be done BEFORE the pool is closed.
        """
        promise = self._pool.apply_async(common.asYAML, (data,))
        self._file_promises[yamlpath].append(promise)

    def write_as_yaml(self, data: Any, yamlpath: Path) -> None:
        """Queue the conversion of this data to YAML and write to file."""
        self._pool.apply_async(common.saveYamlFile, (data, yamlpath))

    def combined_output(self) -> str:
        """Join all the converted chunks into one block of YAML."""
        return "".join(self._chunks)

    def write_combined(self, path: Path) -> None:
        """Write all the converted chunks into one YAML file."""
        self._log.info("Writing %d YAML chunks to %s", len(self._chunks), path)

        with path.open("w") as outfile:
            outfile.write(self.combined_output())

    def write_files(self) -> None:
        """Write all append_as_yaml() files to disk."""
        for yamlpath, promises in self._file_promises.items():
            with yamlpath.open("w") as outfile:
                for promise in promises:
                    outfile.write(promise.get(MULTIPROCESSING_TIMEOUT))

    def __enter__(self) -> "OutputGatherer":
        self._pool.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            # In case of error, don't bother gathering the results.
            return self._pool.__exit__(exc_type, exc_value, traceback)

        try:
            for promise in self._yaml_promises:
                self._chunks.append(promise.get(MULTIPROCESSING_TIMEOUT))
        except KeyboardInterrupt:
            self._pool.terminate()
        else:
            self._pool.close()
        self._pool.join()
