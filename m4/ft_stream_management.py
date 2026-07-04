#!/usr/bin/env python3


"""
Directory: ex2/
Files to Submit: ft_stream_management.py
Authorized: import sys, sys.argv, sys.stdin, sys.stdout, sys.stderr, len(),
open(), import typing, typing.IO, io.read(), io.readline(), io.write(),
io.flush(), io.close(), print()
"""

import sys


def display_stream() -> str | None:
    if len(sys.argv) != 2:
        sys.stdout.write(f"Usage: {sys.argv[0]} <file>\n")
        return None
    content: str | None = None
    file = None
    sys.stdout.write(f"Accesing file'{sys.argv[1]}'\n")
    sys.stdout.flush()
    try:
        file = open(sys.argv[1])
        content = file.read()
        sys.stdout.write(f"---\n\n{content}\n\n---\n")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        return None
    finally:
        if file:
            file.close()
            sys.stdout.write(f"File '{sys.argv[1]}' closed\n")
    return content


def save_stream(content: str) -> None:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    file_name: str = sys.stdin.readline().rstrip("\n")
    if not file_name:
        sys.stdout.write("Not saving data\n")
        return
    file = None
    try:
        sys.stdout.write(f"Saving data to '{file_name}'\n")
        file = open(file_name, "w")
        file.write(content)
        sys.stdout.write(f"Data saved in file '{file_name}'\n")
    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error saving to file '{file_name}': {e}"
            "\ndata not saved\n"
        )
        return
    finally:
        if file:
            file.close()


def ft_stream_management() -> None:
    sys.stdout.write(" ===  Cyber Archives Recovery & Preservation ===\n")
    content: str | None = display_stream()
    if not content:
        return
    sys.stdout.write("\nTransform data: \n")
    new: list[str] = []
    for line in content.splitlines():
        new.append(line + "#")
    content = "\n".join(new)
    sys.stdout.write(f"---\n\n{content}\n\n---\n")
    save_stream(content)


def main() -> None:
    ft_stream_management()
    return


if __name__ == "__main__":
    main()
