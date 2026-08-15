#!/usr/bin/env python3


"""Directory: ex0/.

Files to Submit: ft_command_quest.py
Authorized: import sys, sys.argv, len(), print()
"""

import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) != 1:
        print(f"Arguments received {len(sys.argv) - 1}")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
    else:
        print("No arguments provided!")
    print(f"Total arguments {len(sys.argv)}")


if __name__ == "__main__":
    main()
