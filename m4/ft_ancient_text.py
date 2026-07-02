#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: ft_ancient_text.py
Authorized: import sys, sys.argv, len(), open(), import typing, typing.IO,
io.read(), io.close(), print()
"""

from sys import argv
import typing


def ft_ancient_text(args: list[str]) -> None:
    print("=== Cyber Archives Recovery ===")
    for arg in args:
        try:
            print(f"Accesing {arg}")
            fd = open(arg)
            print("---\n")
            print(fd.read())
            print("\n---")
            typing.IO.close(fd)
            print(f"File '{arg}' closed")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{arg}': {e}")


def main() -> None:
    if len(argv) < 2:
        return print(f"Usage: {argv[0]} <file>")
    args: list[str] = argv[1:]
    ft_ancient_text(args)
    return


if __name__ == "__main__":
    main()
