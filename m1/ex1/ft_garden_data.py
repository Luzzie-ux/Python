#!/usr/bin/env python3

"""
ft_garden_data.py
"""


class Plant:
    """
    Class Plant that defines name, height and age of each plant
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """Prints garden plants information"""
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30).show()
    Plant("Sunflower", 80, 45).show()
    Plant("Cactus", 15, 120).show()


def main() -> None:
    ft_garden_data()


if __name__ == "__main__":
    main()
