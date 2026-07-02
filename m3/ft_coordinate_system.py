#!/usr/bin/env python3


"""
Directory: ex2/
Files to Submit: ft_coordinate_system.py
Authorized: import math, math.sqrt(), input(), round(), print()
"""

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        axis: list[str] = coordinates.split(",")
        if len(axis) != 3:
            print("Invalid syntax")
            continue
        posix: list[float] = []
        error: bool = False
        for x in axis:
            try:
                value: str = x.strip()
                posix.append(float(value))
            except ValueError as e:
                print(f"Error on parameter '{value}': {e}")
                error = True
                break
        if error:
            continue
        return posix[0], posix[1], posix[2]


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    set_1: tuple[float, float, float] = get_player_pos()
    x1: float = set_1[0]
    y1: float = set_1[1]
    z1: float = set_1[2]
    print(f"Got a first tuple: {set_1}")
    print(f"It includes: X={set_1[0]}, Y={set_1[1]}, Z={set_1[2]}")
    sqrt1: float = math.sqrt((x1**2) + (y1**2) + (z1**2))
    print(f"Distance to center: {round(sqrt1, 4)}")
    print("Get a second set of coordinates")
    set_2: tuple[float, float, float] = get_player_pos()
    x2: float = set_2[0]
    y2: float = set_2[1]
    z2: float = set_2[2]
    sqrt2: float = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(sqrt2, 4)}")
    return


def main() -> None:
    ft_coordinate_system()


if __name__ == "__main__":
    main()
