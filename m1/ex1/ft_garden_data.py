#!/usr/bin/env python3

"""
ft_garden_data.py
"""


class Plant():
    """
    Class Plant that defines name, height and age of each plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        return


def ft_garden_data() -> None:
    """
    Main Function
    """
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30).show
    Plant("Sunflower", 80, 45).show
    Plant("Cactus", 15, 120).show
    return


if __name__ == "__main__":
    ft_garden_data()
