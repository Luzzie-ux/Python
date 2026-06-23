#!/usr/bin/env python3

"""
ft_garden_security.py
"""


class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name.capitalize()
        self._height: float = 0.0
        self._age: int = 0
        self.set_att(round(height, 2), age)
        if self._age == age and self._height == height:
            print("Plant created:", end=" ")
            print(f"{self._name}: {self._height}cm, {self._age} days old\n")

    def set_att(self, height: float, age: int) -> None:
        """
        Sets Atributes of the plant if they are  not negative
        """
        if height < 0.0:
            print(f"{self._name}: Error: Height can't be negative")
            print("Height update Rejected")
        if age < 0:
            print(f"{self._name}: Error: Age can't be negative")
            print("Height update Rejected")
            return
        else:
            self._height = height
            self._age = age
        return

    def update(self, height: float, age: int) -> None:
        """
        updates plants attributes but first verifies if they are not negative
        """
        self.set_att(height, age)
        if self._height == height:
            print(f"Height updated: {height}cm")
        if self._age == age:
            print(f"Age updated: {age} days")
        return

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def info(self) -> None:
        """
        Prints to stdout the current state of the plant
        """
        h: float = self.get_height()
        a: int = self.get_age()
        print(f"Current state: {self._name}: {h}cm, {a} days old")
        return


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10)
    plant.update(25, 30)
    print()
    plant.update(-1, -1)
    print()
    plant.info()


if __name__ == "__main__":
    ft_garden_security()
