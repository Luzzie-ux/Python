#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: construct.py
Authorized: sys, os, site modules, print()
"""

import sys, os, site


def is_venv() -> bool:
    if sys.prefix == sys.base_exec_prefix:
        return True
    return False


def main() -> int:
    os.write(1, b"=== Isolated Enviroment Checker ===\n")
    if not is_venv():
        sys.stdout.write(
            "Hello There! You are running this script in a venv!\n"
            f" we can know that because your sys.prefix: {sys.prefix}\n"
            f" is not the same as sys.base_prefix: {sys.base_prefix}\n"
        )
    else:
        sys.stdout.write(
            "Hello There! You are running this script without a venv!\n"
            "In case you want to use one, "
            "type into your terminal the following:\n"
            "\n   python3 -m venv <name_of_venv>\n"
            "   source <name_of_venv>/bin/activate # ON Unix\n"
            "   <name_of_venv>\\Scripts\\activate # On Windows\n"
            "\n(name_of_venv here is a user given name)\n"
        )
    print("Have a good day!")


if __name__ == "__main__":
    main()
