#!/usr/bin/env python3
# Copyright (c) 2026 Luz
# seed inventory

"""Directory: ex7/.

Files to Submit: ft_seed_inventory.py
Authorized: print(), string methods
"""


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """Display seed inventory with inputs from stdin."""
    if unit.lower() == "packets":
        print(
            f"{seed_type.capitalize()} seeds: "
            f"{quantity} {unit.lower()} avaiable",
        )
    elif unit.lower() == "grams":
        print(
            f"{seed_type.capitalize()} seeds: {quantity} {unit.lower()} total",
        )
    elif unit.lower() == "area":
        print(
            f"{seed_type.capitalize()} seeds: covers {quantity} square meters",
        )
    else:
        print("Unknown unit type")
