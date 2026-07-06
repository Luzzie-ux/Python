#!/usr/bin/env python3


"""
ft_command_quest.py
"""

import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) != 1:
        i: int = 1
        print(f"Arguments received {len(sys.argv) - 1}")
        for arg in sys.argv[i:]:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    else:
        print(f"No arguments provided!")
    print(f"Total arguments {len(sys.argv)}")
    return


if __name__ == "__main__":
    main()
