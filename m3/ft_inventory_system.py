#!/usr/bin/env python3


"""
Directory: ex4/
Files to Submit: ft_inventory_system.py
Authorized: import sys, sys.argv, len(), print(), sum(), list(), round(),
dict.keys(), dict.values(), dict.update()
"""

import sys


def parser() -> list[str]:
    args: list[str] = []
    for arg in sys.argv[1:]:
        item: list[str] = arg.split(':')
        if len(item) % 2 != 0:
            print(f"Error - invalid parameter '{arg}'")
            continue
        for i in item:
            args.append(i)
    return args


def inventory_system(args: list[str]) -> dict[str, int]:
    i: int = 0
    key: str
    value: str
    inventory: dict[str, int] = {}
    while i < len(args):
        key: str = args[i]
        value: str = args[i + 1]
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            i += 2
            continue
        try:
            inventory[key.strip(",")] = int(value.strip(","))
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
        i += 2
    return inventory


def main() -> None:
    if len(sys.argv) < 2:
        return
    print("=== Inventory System Analysis ===")
    args: list[str] = parser()
    bag: dict[str, int] = inventory_system(args)
    print(f"Got inventory: {bag}")
    keys: list[str] = []
    for key in bag.keys():
        keys.append(key)
    print(f"Item list: {keys}")
    t_key: int = len(bag.keys())
    t_value: int = sum(bag.values())
    print(f"Total quantity of the {t_key} items: {t_value}")
    chest: list[str] = list(bag.keys())
    most: str = chest[0]
    least: str = chest[0]
    for item in bag:
        if bag[item] > bag[most]:
            most = item
        elif bag[item] < bag[least]:
            least = item
        print(
            f"Item {item} represents "
            f"{round(bag[item] / t_value * 100,2)}%"
              )
    print(f"Item most abundant: {most} with quantity {bag[most]}")
    print(f"Item least abundant: {least} with quantity {bag[least]}")
    bag.update({"magic_item": 1})
    print(f"Updated inventory: {bag}")
    return


if __name__ == "__main__":
    main()


"""
> python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
=== Inventory System Analysis ===
Redundant item 'sword'- discarding
Error - invalid parameter 'hello'
Quantity error for 'key': invalid literal for int() with base 10: 'value'
Got inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1}
Item list: ['sword', 'potion', 'shield', 'armor', 'helmet']
Total quantity of the 5 items: 12
Item sword represents 8.3%
Item potion represents 41.7%
Item shield represents 16.7%
Item armor represents 25.0%
Item helmet represents 8.3%
Item most abundant: potion with quantity 5
Item least abundant: sword with quantity 1
Updated inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1, 'magic_item': 1}
"""