#!/usr/bin/env python3


"""
Directory: ex4/
Files to Submit: ft_inventory_system.py
Authorized: import sys, sys.argv, len(), print(), sum(), list(), round(),
dict.keys(), dict.values(), dict.update()
"""

import sys


def parser(args: list[str]) -> dict:
    result: dict = {}
    for arg in args:
        try:
            parts: list = arg.split(':')
            if len(parts) != 2:
                print(f"Error - invalid parameter '{arg}'")
                continue
            key: str  = parts[0]
            value: str = parts[1]
            if key in result:
                print(f"Redundant item '{key}' - discarding")
                continue
            result[key.strip(",")] = int(value.strip(","))
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    return result

def ft_inventory_system() -> None:
    if len(sys.argv) < 2:
        return
    print("=== Inventory System Analysis ===")
    bag: dict = parser(sys.argv[1:])
    print(f"Got bag: {bag}")
    t_key: int = len(bag.keys())
    t_value: int = sum(bag.values())
    print(f"Total quantity of the {t_key} items: {t_value}")
    for item in bag:
        print(
            f"Item {item} represents "
            f"{round(bag[item] / t_value * 100, 1)}%"
        )
    inventory: list = list(bag.keys())
    least: str = inventory[0]
    most: str = inventory[0]
    for i in bag:
        if bag[least] < bag[i]:
            least = i
        elif bag[most] > bag[i]:
            most = i
    print(f"Item most abundant: {least} with quantity {bag[least]}")
    print(f"Item least abundant: {most} with quantity {bag[most]}")
    bag.update({"magic item": 1})
    print(f"Updated inventory: {bag}")
    return


def main() -> None:
    ft_inventory_system()
    return


if __name__ == "__main__":
    main()
