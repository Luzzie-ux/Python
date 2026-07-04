#!/usr/bin/env python3


"""
Directory: ex1/
Files to Submit: ft_archive_creation.py
Authorized: import sys, sys.argv, len(), open(), import typing, typing.IO,
io.read(), io.write(), io.close(), print(), input()
"""

import sys


def display_stream() -> str | None:
    if len(sys.argv) != 2:
        return print(f"Usage: {sys.argv[0]} <file>")
    content: str | None = None
    file = None
    print(f"Accesing file'{sys.argv[1]}'")
    try:
        file = open(sys.argv[1])
        content = file.read()
        print(f"---\n\n{content}\n\n---")
    except Exception as e:
        return print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file:
            file.close()
            print(f"File '{sys.argv[1]}' closed\n")
    return content


def save(content: str) -> None:
    print("Enter new file name (or empty):", end=" ")
    file_name: str = input()
    f = None
    if not file_name:
        return print("Not saving data")
    try:
        print(f"Saving data to '{file_name}'")
        f = open(file_name, "w")
        f.write(content)
        print(f"Data saved in file '{file_name}'")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
    finally:
        if f:
            f.close()


def ft_archive_creation() -> None:
    print(" ===  Cyber Archives Recovery & Preservation ===")
    content: str | None = display_stream()
    if not content:
        return
    print("Transform data: ")
    new: list[str] = []
    for line in content.splitlines():
        new.append(line + "#")
    content = "\n".join(new)
    print(f"---\n\n{content}\n\n---")
    save(content)


def main() -> None:
    ft_archive_creation()
    return


if __name__ == "__main__":
    main()
