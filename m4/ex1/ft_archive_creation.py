#!/usr/bin/env python3


"""
Directory: ex1/
Files to Submit: ft_archive_creation.py
Authorized: import sys, sys.argv, len(), open(), import typing, typing.IO,
io.read(), io.write(), io.close(), print(), input()
"""

import sys
import typing


def save(content: str) -> None:
    name: str = input("Enter new file name (or empty): ")
    if not name:
        return print("Not saving data.")
    print(f"Saving data to '{name}'")
    file: typing.IO[str] | None = None
    try:
        file = open(name, "w")
        file.write(content)
    except PermissionError as e:
        print(f"Error opening file {name}: {e}")
    finally:
        if file:
            file.close()
            print(f"Data saved in file '{name}'")
    return


def transform(text: str) -> None:
    print("\nTransform data:\n")
    new: list[str] = []
    for line in text.splitlines():
        new.append(line + "#")
    content: str = "\n".join(new)
    print(f"\n---\n\n{content}\n\n---\n")
    save(content)
    return


def main() -> None:
    argc: int = len(sys.argv)
    if not argc == 2:
        return print(f"Usage: {sys.argv[0]} <file>")
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"accessing file '{sys.argv[1]}'")
    file: typing.IO[str] | None = None
    data: str | None = None
    try:
        file = open(sys.argv[1])
        data = file.read()
        print(f"\n---\n\n{data}\n\n---\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file:
            file.close()
        print(f"File '{sys.argv[1]}' closed.")
    if data:
        transform(data)
    return


if __name__ == "__main__":
    main()
