#!/usr/bin/env python3
# Copyright (c) 2026 Luz
# count harvest iterative

"""Directory: ex6/.

Files to Submit: ft_count_harvest_iterative.py, ft_count_harvest_recursive.py
Authorized: input(), int(), print(), range(), defining helper functions for
recursion.
"""


def ft_count_harvest_iterative() -> None:
    """Count how many days till harvest."""
    i = 1
    days = int(input("Days until harvest: "))
    while i < days + 1:
        print(f"Day {i}")
        if i == days:
            print("Harvest time!")
        i += 1
