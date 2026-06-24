#!/usr/bin/env python3

"""
ft_plant_factory.py
"""


class Plant:
    """
    Plant class composed of name, initial height and initial age.
    """

    def __init__(self, name: str, height: float, age: int, mod: float) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.mod: float = mod
        self.initial_height: float = height

    def show(self) -> None:
        """
        Shows plant information at the start of the script
        """
        print(f"{self.name}: is {self.height}cms and {self.age} days old")
        return

    def grow(self) -> None:
        """
        Adds modifier to height
        """
        self.height = round(self.height + self.mod, 2)
        return

    def aging(self) -> None:
        """
        Adds one to age
        """
        self.age = self.age + 1
        return

    def simulate(self) -> None:
        """
        Displays plant status in loop iterating grow and age,
        showing every stage until 7, then at the end shows
        "total growth" of the plant after the loop is done
        """
        print(f" --- {self.name} status: ---")
        for days in range(1, 8):
            self.grow()
            self.aging()
            print(f"=== Day: {days} ===")
            self.show()
        total: float = round(self.height - self.initial_height, 2)
        print(f"\n{self.name} total growth after 7 days: {total}cm\n")
        return


def ft_plant_factory() -> None:
    """Creates plants and prints it's growth cycle"""
    print("\n=== Factory Input ===\n")
    plants: list[Plant] = [
        Plant("Rose", 5.0, 10, 1.5),
        Plant("Sunflower", 30.0, 23, 15.0),
        Plant("Cactus", 1.0, 0, 12.0),
        Plant("Tulip", 2.5, 3, 8.0),
        Plant("Fern", 1.0, 6, 0.7),
    ]
    for plant in plants:
        plant.show()
    print("\n=== Factory Output ===\n")
    for plant in plants:
        plant.simulate()
    return


if __name__ == "__main__":
    ft_plant_factory()
