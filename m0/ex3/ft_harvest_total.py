# Copyright (c) 2026 Luz
# harvest total

"""
Directory: ex3/
Files to Submit: ft_harvest_total.py
Authorized: input(), int(), print()
"""


def ft_harvest_total() -> None:
    """
    function that counts how much was harvested in three days
    """
    w1 = int(input("Day 1 harvest: "))
    w2 = int(input("Day 2 harvest: "))
    w3 = int(input("Day 3 harvest: "))

    total = w1 + w2 + w3
    print(f"Total harvest: {total}")
