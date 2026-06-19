#!/usr/bin/env python3

"""
Defines Class Plant with new parameters, and new functions inside class
that will help simulate plant growth over time
"""


class Plant():
    """
    Plant class that will define name, age, height, modifier and initial_height
    as Plant parameters, and then define four functions:
    grow(), age(), show() and simulate()
    """
    def __init__(self, name: str, old: int, height: float, modifier: float):
        self.name = name
        self.old = old
        self.height = height
        self.modifier = modifier
        self.initial_height = height

    def show(self) -> None:
        """
        Shows plant information at the start of the script
        """
        print(f"{self.name}: is {self.height}cms and {self.old} days old")
        return

    def grow(self) -> None:
        """
        Addes modifier with height every time its called with a 2 decimals
        """
        self.height = round(self.height + self.modifier, 2)
        return

    def age(self) -> None:
        """
        Addeds 1 to old every time its called
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
    """
    Main Function
    """
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
