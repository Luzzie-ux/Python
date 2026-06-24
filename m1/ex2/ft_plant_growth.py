#!/usr/bin/env python3

"""
ft_plant_growth.py
"""


class Plant():
    """
    Plant class that will define name, age, height, mod and initial_height
    as Plant parameters, and then define four functions:
    grow(), age(), show() and simulate()
    """
    def __init__(self, name: str, old: int, height: float, mod: float) -> None:
        self.name: str = name
        self.old: int = old
        self.height: float = height
        self.mod: float = mod
        self.initial_height: float = height

    def show(self) -> None:
        """
        Shows plant information at the start of the script
        """
        print(f"{self.name}: is {self.height}cms and {self.old} days old")
        return

    def grow(self) -> None:
        """
        Adds modifier to height
        """
        self.height = round(self.height + self.mod, 2)
        return

    def age(self) -> None:
        """
        Adds one to age
        """
        self.old = self.old + 1
        return

    def simulate(self) -> None:
        """
        Displays plant status in loop iterating grow and age,
        showing every stage until 7, then at the end shows
        "total growth" of the plant after the loop is done
        """
        print(f" --- {self.name} status: ---")
        self.show()
        for days in range(1, 8):
            self.grow()
            self.age()
            print(f"=== Day: {days} ===")
            self.show()
        total = round(self.height - self.initial_height, 2)
        print(f"Total growth after 7 days: {total}cm\n")
        return


def ft_plant_growth() -> None:
    """Prints the garden plants growth cycle"""
    print("=== Garden Plant Growth ===")
    rose = Plant("Roses", 10, 25, 0.8)
    rose.simulate()
    sunflower = Plant("Sunflowers", 5, 11, 2.5)
    sunflower.simulate()
    violet = Plant("Violets", 15, 5, 1.0)
    violet.simulate()
    return


if __name__ == "__main__":
    ft_plant_growth()
