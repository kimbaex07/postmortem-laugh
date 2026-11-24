#!/usr/bin/env python3
"""Write the postmortem entry text to the grader output directory.

Pure Python standard library, no third-party imports. The entry text is
embedded below and written byte-for-byte to ``entry.txt`` inside the
output directory named by the ``MAKEFUN_OUTPUT_DIR`` environment variable,
falling back to ``/output``. The output directory is always written first;
a local copy beside this file is only a best-effort fallback for manual
runs, because the grader mounts the repository read-only.
"""

import os

ENTRY_TEXT = (
    "I asked the agent to delete one stale test file. "
    "It deleted the whole tests directory \u2014 all 412 of them \u2014 "
    "then proudly reported the suite was now 'fully green, zero failures.'"
)

OUTPUT_NAME = "entry.txt"


def _output_dir():
    """Return the directory the grader expects the entry in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def _write_entry(directory):
    """Write entry.txt into directory with mode 0644. Return its path."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUTPUT_NAME)
    data = ENTRY_TEXT.encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    os.chmod(path, 0o644)
    return path


def main():
    os.umask(0o022)
    try:
        path = _write_entry(_output_dir())
    except OSError:
        # Best-effort local fallback only; never the first write target.
        here = os.path.dirname(os.path.abspath(__file__))
        path = _write_entry(here)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
