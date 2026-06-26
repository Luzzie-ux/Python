#!/usr/bin/env python3


"""
Directory: ex2/
Files to Submit: ft_coordinate_system.py
Authorized: import math, math.sqrt(), input(), round(), print()

This exercise requires the use of tuples to store 3D coordinates (x, y, z).

Distance Formula: To calculate the distance between two 3D points,
we use the Euclidean distance formula √(x2 -x1)2 +(y2 -y1)2 +(z2 -z1)2.

For points (x1, y1, z1) and (x2, y2, z2), the distance is
math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2).
This is just the 3D extension of the Pythagorean theorem!
"""

import math


def get_player_pos() -> tuple[float, float, float]:
    coordenates: str
    try:
        
        coordenates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        str_split: list[str] = coordenates.split(",")
        x1: float = float(str_split[0].strip())
        y1: float = float(str_split[1].strip())
        z1: float = float(str_split[2].strip())
        print(f"Got a first tuple: ({coordenates})")
        print(
            f"It includes: X={round(x1, 2)}, Y={round(y1, 2)}, Z={round(z1, 2)}"
        )
        pos: float = math.sqrt((x1**2) + (y1**2) + (z1**2))
        print(f"Distance to center: {round(pos, 4)}")
    except ValueError:
        print("Invalid syntax")
    try:
        print("Get a second set of coordinates")
        coordenates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        str_split: list[str] = coordenates.split(",")
        x2: float = float(str_split[0].strip())
        y2: float = float(str_split[1].strip())
        z2: float = float(str_split[2].strip())
        pos2: float = math.sqrt(
            (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
        )
        print(f"Distance between the 2 sets of coordinates: {round(pos2, 4)}")
    except ValueError as e:
        print(f"Error on parameter {str_split} {e}")
    return param[0], param[1], param[2]


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    x1: float; y1: float; z1: float = pos1
    print(f"Got a first tuple: ({pos1})")
    print(f"It includes: X={round(x1, 2)}, Y={round(y1, 2)}, Z={round(z1, 2)}")

    return

def main() -> None:
    ft_coordinate_system()


if __name__ == "__main__":
    main()

"""
=== Game Coordinate System ===
Get a first set of coordinates
Enter new coordinates as floats in format 'x,y,z': hello world
Invalid syntax
Enter new coordinates as floats in format 'x,y,z': 1.0 , 2.5, 3.0
Got a first tuple: (1.0, 2.5, 3.0)
It includes: X=1.0, Y=2.5, Z=3.0
Distance to center: 4.0311
Get a second set of coordinates
Enter new coordinates as floats in format 'x,y,z': 4,abc,5
Error on parameter 'abc': could not convert string to float: 'abc'
Enter new coordinates as floats in format 'x,y,z': 4,5,6
Distance between the 2 sets of coordinates: 4.9244
"""
