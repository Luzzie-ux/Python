#!/usr/bin/env python3
# Copyright (c) 2026 Luz
# plot area

"""Directory: ex2/.

Files to Submit: ft_plot_area.py
Authorized: input(), int(), print().
"""


def ft_plot_area() -> None:
    """Calculate plot area with lenght and width from stdin."""
    length = int(input("Enter length: "))
    wid = int(input("Enter width: "))
    area = length * wid
    print(f"Plot area: {area}")
