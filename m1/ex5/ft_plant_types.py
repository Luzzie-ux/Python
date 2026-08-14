#!/usr/bin/env python3
# Copyright (c) 2026 Luz

"""irectory: ex5/.

Files to Submit: ft_plant_types.py
Authorized: super(), print(), range(), round().
"""


class Plant:
    """Plant class composed of name, initial height and initial age."""

    def __init__(self, name: str, height: float, age: int, mod: float) -> None:
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
        mod : float
            mod: plant growth rate

        """
        self._name: str = name.capitalize()
        self._height: float = 0.0
        self._age: int = 0
        self.mod: float = mod
        self.set_att(round(height, 2), age)

    def grow(self) -> None:
        """TODO: describe grow.

        TODO: add description.
        """
        self._height = round(self._height + self.mod, 2)
        self._age += 1

    def set_att(self, height: float, age: int) -> None:
        """TODO: describe set_att.

        TODO: add description.

        Parameters
        ----------
        height : TODO
            TODO: describe height
        age : TODO
            TODO: describe age

        """
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
        """TODO: describe update.

        TODO: add description.

        Parameters
        ----------
        height : TODO
            TODO: describe height
        age : TODO
            TODO: describe age

        """
        self.set_att(height, age)
        if self._height == height:
            print(f"Height updated: {height}cm")
        if self._age == age:
            print(f"Age updated: {age} days")

    def show(self) -> None:
        """TODO: describe show.

        TODO: add description.
        """
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    """TODO: describe Flower.

    TODO: add description.
    """

    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        mod: float,
        color: str,
    ) -> None:
        """TODO: describe __init__.

        TODO: add description.

        Parameters
        ----------
        name : TODO
            TODO: describe name
        age : TODO
            TODO: describe age
        height : TODO
            TODO: describe height
        mod : TODO
            TODO: describe mod
        color : TODO
            TODO: describe color

        """
        super().__init__(name, height, age, mod)
        self._color: str = color
        self._bloom: bool = False

    def show(self) -> None:
        """Display Plant."""
        super().show()
        print(f"Color: {self._color}")
        self.bloom()

    def bloom(self) -> None:
        """Asks the Flower to bloom if it hasn't already."""
        if not self._bloom:
            self._bloom = True
            print(f"{self._name} has not bloomed yet")
            print(f"[asking the {self._name.lower()} to bloom]")
            self.show()
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    """TODO: describe Tree.

    TODO: add description.
    """

    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        mod: float,
        trunk_diameter: float,
    ) -> None:
        """TODO: describe __init__.

        TODO: add description.

        Parameters
        ----------
        name : TODO
            TODO: describe name
        age : TODO
            TODO: describe age
        height : TODO
            TODO: describe height
        mod : TODO
            TODO: describe mod
        trunk_diameter : TODO
            TODO: describe trunk_diameter

        """
        super().__init__(name, height, age, mod)
        self._diameter: float = trunk_diameter

    def show(self) -> None:
        """TODO: describe show.

        TODO: add description.
        """
        super().show()
        print(f"Trunk diameter: {self._diameter}cm")
        self.produce_shade()

    def produce_shade(self) -> None:
        """Asks the Tree to produce a shade."""
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}cm", end=" ")
        print(f"long and {self._diameter}cm wide.")


class Vegetable(Plant):
    """TODO: describe Vegetable.

    TODO: add description.
    """

    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        mod: float,
        harvest_season: str,
    ) -> None:
        """TODO: describe __init__.

        TODO: add description.

        Parameters
        ----------
        name : TODO
            TODO: describe name
        age : TODO
            TODO: describe age
        height : TODO
            TODO: describe height
        mod : TODO
            TODO: describe mod
        harvest_season : TODO
            TODO: describe harvest_season

        """
        super().__init__(name, height, age, mod)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = 0

    def show(self) -> None:
        """TODO: describe show.

        TODO: add description.
        """
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, days: int) -> None:
        """Make the Vegetable age for a certain amount of time."""
        for _i in range(days):
            super().grow()
            self._nutritional_value += 1
        print(f"[make {self._name} grow and age for {days} days]")
        self.show()


def ft_plant_types() -> None:
    """Print the plants types and their information."""
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("rose", 10, 15, 0.5, "red")
    rose.show()
    print("=== Tree")
    oak: Tree = Tree("oak", 365, 200.00, 40.6, 5.0)
    oak.show()
    print("=== Vegetable")
    tomato: Vegetable = Vegetable("tomato", 10, 5.0, 2.10, "april")
    tomato.show()
    tomato.age(20)


def main() -> None:
    """TODO: describe main.

    TODO: add description.
    """
    ft_plant_types()


if __name__ == "__main__":
    main()
