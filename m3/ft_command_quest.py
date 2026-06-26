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
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")


def main() -> None:
    ft_command_quest()


if __name__ == "__main__":
    ft_command_quest()
