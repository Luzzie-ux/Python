# Copyright (c) 2026 Luz
# water reminder

"""
Directory: ex5/
Files to Submit: ft_water_reminder.py
Authorized: input(), int(), print()
"""


def ft_water_reminder() -> None:
    """
    function that reminds to water plants
    """
    max_days: int = 2
    dry = int(input("Days since last watering: "))
    if dry > max_days:
        print("Water the plants!")
    else:
        print("Plants are fine")
