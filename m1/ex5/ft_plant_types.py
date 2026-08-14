#!/usr/bin/env python3

"""
irectory: ex5/
Files to Submit: ft_plant_types.py
Authorized: super(), print(), range(), round()
"""


class Plant:
    def __init__(self, name: str, height: float, age: int, mod: float) -> None:
        self._name: str = name.capitalize()
        self._height: float = 0.0
        self._age: int = 0
        self.mod: float = mod
        self.set_att(round(height, 2), age)

    def grow(self) -> None:
        self._height = round(self._height + self.mod, 2)
        self._age += 1

    def set_att(self, height: float, age: int) -> None:
        if height < 0.0:
            print(f"{self._name}: Error: Height can't be negative")
            print("Height update Rejected")
        if age < 0:
            print(f"{self._name}: Error: Age can't be negative")
            print("Age update Rejected")
            return
        self._height = height
        self._age = age
        return

    def update(self, height: float, age: int) -> None:
        self.set_att(height, age)
        if self._height == height:
            print(f"Height updated: {height}cm")
        if self._age == age:
            print(f"Age updated: {age} days")

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        mod: float,
        color: str,
        bloom: bool = False,
    ) -> None:
        super().__init__(name, height, age, mod)
        self._color: str = color
        self._bloom: bool = bloom

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        self.bloom()

    def bloom(self) -> None:
        """
        Asks the Flower to bloom if it hasn't already
        """
        if not self._bloom:
            self._bloom = True
            print(f"{self._name} has not bloomed yet")
            print(f"[asking the {self._name.lower()} to bloom]")
            self.show()
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        mod: float,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age, mod)
        self._diameter: float = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._diameter}cm")
        self.produce_shade()

    def produce_shade(self) -> None:
        """
        Asks the Tree to produce a shade
        """
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}cm", end=" ")
        print(f"long and {self._diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        mod: float,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        super().__init__(name, height, age, mod)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, days: int) -> None:
        """
        Makes the Vegetable age for a certain amount of time given as param
        """
        for _i in range(days):
            super().grow()
            self._nutritional_value += 1
        print(f"[make {self._name} grow and age for {days} days]")
        self.show()


def ft_plant_types() -> None:
    """Prints the plants types and their information"""
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("rose", 10, 15, 0.5, "red")
    rose.show()
    print("=== Tree")
    oak: Tree = Tree("oak", 365, 200.00, 40.6, 5.0)
    oak.show()
    print("=== Vegetable")
    tomato: Vegetable = Vegetable("tomato", 10, 5.0, 2.10, "april", 0)
    tomato.show()
    tomato.age(20)


def main() -> None:
    ft_plant_types()


if __name__ == "__main__":
    main()
