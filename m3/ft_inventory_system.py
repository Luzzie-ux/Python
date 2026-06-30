#!/usr/bin/env python3


"""
Directory: ex4/
Files to Submit: ft_inventory_system.py
Authorized: import sys, sys.argv, len(), print(), sum(), list(), round(),
dict.keys(), dict.values(), dict.update()
"""

import sys

# Each parameter must follow this format: <item_name>:<quantity>
def ft_inventory_system() -> None:
    size: int = len(sys.argv)
    if size < 2:
        return
    print("=== Inventory System Analysis ===")
    args: list[str] = sys.argv[1:]
    items: list[str] = []
    bad_arg: list[str] = []
    for arg in args:
        if ":" not in arg:
            bad_arg.append(arg)
        items.extend(arg.split(":"))
    for item in items:
        for i in items[1:]:
            if item == i:
                print(f"Redundant item {item} discarding")

    print(f"Error - invalid parameter {bad_arg}")
    return


def main() -> None:
    ft_inventory_system()
    return


if __name__ == "__main__":
    main()
