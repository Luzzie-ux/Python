#!/usr/bin/env python3

"""
ft_plant_types.py
"""


class Plant():
    def __init__(self, name: str, height: float, age: int, mod: float):
        self._name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self.mod = mod
        self.set_att(round(height, 2), age)
        if self._age == age and self._height == height:
            print("Plant created:", end=" ")
            print(f"{self._name}: {self._height}cm, {self._age} days old\n")

    def grow(self) -> None:
        """
        Addes modifier with height every time its called with a 2 decimals
        """
        self.height = round(self.height + self.mod, 2)
        return

    def aging(self) -> None:
        """
        Addeds 1 to old every time its called
        """
        self.age += 1
        return

    def set_att(self, height: float, age: int) -> None:
        """
        Sets Atributes of the plant if they are  not negative
        """
        if height < 0.0:
            print(f"{self._name}: Error: Height can't be negative")
            print("Height Update Rejected")
        if age < 0:
            print(f"{self._name}: Error: Age can't be negative")
            print("Height Update Rejected")
            return
        else:
            self._height = height
            self._age = age
        return

    def Update(self, height: float, age: int) -> None:
        """
        Updates plants attributes but first verifies if they are not negative
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

    def Info(self) -> None:
        """
        Prints to stdout the current state of the plant
        """
        h: float = self.get_height()
        a: int = self.get_age()
        print(f"Current state: {self._name}: {h}cm, {a} days old")
        return


class Flower(Plant):
    def __init__(self, name: str, age: int, height: float, mod: float,
                 color: str, isBloom: bool = False):
        super().__init__(name, height, age, mod)
        self._color = color
        self._isBloom = isBloom


class Tree(Plant):
    pass


class Vegetable(Plant):
    pass


def ft_plant_types():
    pass


if __name__ == "__main__":
    ft_plant_types()
