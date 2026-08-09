#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: ft_ancient_text.py
Authorized: import sys, sys.argv, len(), open(), import typing, typing.IO,
io.read(), io.close(), print()
"""

import sys
import typing

MAX_ARGS = 2


def main() -> None:
    argc: int = len(sys.argv)
    if argc != MAX_ARGS:
        return print(f"Usage: {sys.argv[0]} <file>")
    print("=== Cyber Archives Recovery ===")
    print(f"accessing file '{sys.argv[1]}'")
    file: typing.IO[str] | None = None
    try:
        file = open(sys.argv[1], encoding="utf-8")
        data: str = file.read()
        print(f"\n---\n\n{data}\n\n---\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file:
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
    return None


if __name__ == "__main__":
    main()
