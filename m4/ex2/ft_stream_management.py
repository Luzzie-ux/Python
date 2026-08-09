#!/usr/bin/env python3


"""
Directory: ex2/
Files to Submit: ft_stream_management.py
Authorized: import sys, sys.argv, sys.stdin, sys.stdout, sys.stderr, len(),
open(), import typing, typing.IO, io.read(), io.readline(), io.write(),
io.flush(), io.close(), print()
"""

from sys import argv, stderr, stdin, stdout
from typing import IO

MAX_ARGS = 2


def save(content: str) -> int:
    stdout.write("Enter new file name (or empty): ")
    stdout.flush()
    name: str = stdin.readline().strip("\n")
    if not name:
        return stdout.write("Not saving data.\n")
    stdout.write(f"Saving data to '{name}'\n")
    file: IO[str] | None = None
    try:
        file = open(name, "w", encoding="utf-8")
        file.write(content)
    except PermissionError as e:
        stderr.write(
            f"[STDERR] Error opening file {name}: {e}\nData not saved\n",
        )
    finally:
        if file:
            file.close()
            stdout.write(f"Data saved in file '{name}'\n")
    return 0


def transform(text: str) -> None:
    stdout.write("\nTransform data:\n")
    new: list[str] = [line + "#" for line in text.splitlines()]
    content: str = "\n".join(new)
    stdout.write(f"\n---\n\n{content}\n\n---\n")
    save(content)


def main() -> None:
    if len(argv) != MAX_ARGS:
        return
    stdout.write("=== Cyber Archives Recovery & Preservation === \n")
    stdout.write(f"accessing file '{argv[1]}'\n")
    file: IO[str] | None = None
    data: str | None = None
    try:
        file = open(argv[1], encoding="utf-8")
        data = file.read()
        stdout.write(f"---\n\n{data}\n\n---\n")
    except (FileNotFoundError, PermissionError) as e:
        stderr.write(f"[STDERR] Error opening file '{argv[1]}': {e}\n")
    finally:
        if file:
            file.close()
            stdout.write(f"File '{argv[1]}' closed\n")
    if data:
        transform(data)
    return


if __name__ == "__main__":
    main()
