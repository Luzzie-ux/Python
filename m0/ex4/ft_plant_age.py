#!/usr/bin/env python3
# Copyright (c) 2026 Luz
# plant age

"""Directory: ex4/.

Files to Submit: ft_plant_age.py
Authorized: input(), int(), print().
"""


def ft_plant_age() -> None:
    """Display if plant is ready to harvest."""
    ready_to_harvest: int = 60
    age = int(input("Enter plant age in days: "))
    if age > ready_to_harvest:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
