#!/usr/bin/env python3

"""
Directory: ex0/
Files to Submit: ft_command_quest.py
Authorized: import sys, sys.argv, len(), print()
"""

import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Command name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")
    return


def main() -> None:
    ft_command_quest()


if __name__ == "__main__":
    main()
