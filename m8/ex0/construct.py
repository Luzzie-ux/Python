#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: construct.py
Authorized: sys, os, site modules, print()
"""

import sys, os


def main() -> int:
    os.write(1, b"=== Isolated Enviroment Checker ===\n")
    if sys.prefix != sys.base_prefix:
        return sys.stdout.write(
            "Hello There! You are running this script in a venv!\n"
            f" we can know that because your sys.prefix: {sys.prefix}\n"
            f" is not the same as sys.base_prefix: {sys.base_prefix}\n"
        )
    sys.stdout.write("Hello There! You are running this script without a venv!\n")
    print(
        "In case you want to use one, "
        "type into your terminal the following:\n"
        "\n   python3 -m venv <name_of_venv>\n"
        "   source <name_of_venv>/bin/activate\n"
        "\n(name_of_venv here is a user given name)"
    )
    print("Have a good day!")


if __name__ == "__main__":
    main()
