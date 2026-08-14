#!/usr/bin/env python3
# Copyright (c) 2026 Luz

"""Directory: ex1/.

Files to Submit: ft_garden_data.py
Authorized: print().
"""


class Plant:
    """Class Plant that defines name, height and age of each plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Plant class __init__.

        Plant: Class plant that will has, name, heiight and age.

        Parameters
        ----------
        name : str
            name: plant name
        height : float
            height: plant height
        age : int
            age: plant age

        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        """TODO: describe show.

        TODO: add description.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """Print garden plants information."""
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30).show()
    Plant("Sunflower", 80, 45).show()
    Plant("Cactus", 15, 120).show()


def main() -> None:
    """TODO: describe main.

    TODO: add description.
    """
    ft_garden_data()


if __name__ == "__main__":
    main()
