#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: ft_ancient_text.py
Authorized: import sys, sys.argv, len(), open(), import typing, typing.IO,
io.read(), io.close(), print()
"""

import sys


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        return print(f"Usage: {sys.argv[0]} <file>")
    print(" ===  Cyber Archives Recovery ===")
    file = None
    print(f"Accesing file'{sys.argv[1]}'")
    try:
        file = open(sys.argv[1])
        print(f"---\n\n{file.read()}\n\n---")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file:
            file.close()
            print(f"File '{sys.argv[1]}' closed")


def main() -> None:
    ft_ancient_text()
    return


if __name__ == "__main__":
    main()
