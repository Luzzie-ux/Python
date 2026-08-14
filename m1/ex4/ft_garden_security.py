#!/usr/bin/env python3
# Copyright (c) 2026 Luz

"""Directory: ex4/.

Files to Submit: ft_garden_security.py
Authorized: print(), range(), round().
"""


class Plant:
    """Plant class composed of name, initial height and initial age."""

    def __init__(self, name: str, height: float, age: int) -> None:
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
        self._name: str = name.capitalize()
        self._height: float = 0.0
        self._age: int = 0
        self.set_att(round(height, 2), age)
        if self._age == age and self._height == height:
            print("Plant created:", end=" ")
            print(f"{self._name}: {self._height}cm, {self._age} days old\n")

    def set_att(self, height: float, age: int) -> None:
        """Set Attributes of the plant if they are not negative."""
        if height < 0.0:
            print(f"{self._name}: Error: Height can't be negative")
            print("Height update Rejected")
        if age < 0:
            print(f"{self._name}: Error: Age can't be negative")
            print("Height update Rejected")
            return
        self._height = height
        self._age = age
        return

    def update(self, height: float, age: int) -> None:
        """Update plants attributes.

        but first verifies if they are not negative.
        """
        self.set_att(height, age)
        if self._height == height:
            print(f"Height updated: {height}cm")
        if self._age == age:
            print(f"Age updated: {age} days")

    def get_height(self) -> float:
        """Get the height when called.

        Parameter:
        ---------
        self: Class

        Returns
        -------
        float
            is height

        """
        return self._height

    def get_age(self) -> int:
        """Get the age when called.

        Parameter:
        ---------
        self: Class

        Returns
        -------
        int
            age

        """
        return self._age

    def info(self) -> None:
        """TODO: describe info.

        TODO: add description.
        """
        h: float = self.get_height()
        a: int = self.get_age()
        print(f"Current state: {self._name}: {h}cm, {a} days old")


def ft_garden_security() -> None:
    """Print the security system working."""
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10)
    plant.update(25, 30)
    print()
    plant.update(-1, -1)
    print()
    plant.info()


def main() -> None:
    """TODO: describe main.

    TODO: add description.
    """
    ft_garden_security()


if __name__ == "__main__":
    main()
