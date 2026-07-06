#!/usr/bin/env python3


"""
Directory: ex2/
Files to Submit: ft_coordinate_system.py
Authorized: import math, math.sqrt(), input(), round(), print()
"""

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        cin: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        axis: list[str] = cin.split(",")
        if len(axis) < 3:
            print("Invalid syntax")
            continue
        coordinates: list[float] = []
        error = False
        for value in axis:
            try:
                coordinates.append(float(value.strip(" ")))
            except ValueError as e:
                print(f"Error on parameter {value}: {e}")
                error = True
                break
        if error:
            continue
        return coordinates[0], coordinates[1], coordinates[2]


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    x1, y1, z1 = pos1
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x1} Y={y1} Z={z1}")
    dis: float = math.sqrt((x1**2) + (y1**2) + (z1**2))
    print(f"Distance to center: {round(dis, 4)}")
    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    x2, y2, z2 = pos2
    con: float = math.sqrt(
        ((x1 - x1) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2)
    )
    print(f"Distance between the 2 sets of coordinates: {round(con, 4)}")
    return


if __name__ == "__main__":
    main()
