#!/usr/bin/env python3
# Copyright (c) 2026 Luz

"""AutoDoc or AutoDocumenting.

The purpose of this Script is to understand the way python handles
file descriptors, file operations and ruff/ty rule checking
for python files, mostly to also save myself from having to
manually correcting every single thing ruff is saying it's wrong
"""

import sys
from pathlib import Path

MAX_ARGS: int = 2


def main() -> None:
    """Entry point of the script."""
    if len(sys.argv) != MAX_ARGS:
        print(f"Usage: python {__file__} <folder>", file=sys.stderr)
        sys.exit(0)
    folder: Path = Path(sys.argv[1])
    if not folder.is_dir():
        print(f"{folder} is not a valid dir", file=sys.stderr)
        sys.exit(1)
    print(folder)


if __name__ == "__main__":
    main()
