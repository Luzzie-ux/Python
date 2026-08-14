# Copyright (c) 2026 Luz
# count harverst recursive

"""
Directory: ex6/
Files to Submit: ft_count_harvest_iterative.py, ft_count_harvest_recursive.py
Authorized: input(), int(), print(), range(), defining helper functions for
recursion
"""


def recursion_helper(days: int, i: int) -> None:
    """
    helper to allow the counting with recursion
    """
    if i != days + 1:
        print(f"Day {i}")
        i += 1
        recursion_helper(days, i)
    else:
        print("Harvest time!")


def ft_count_harvest_recursive() -> None:
    """
    function that will call recursion helper to count
    """
    i: int = 1
    days: int = int(input("Days until harvest: "))
    recursion_helper(days, i)
