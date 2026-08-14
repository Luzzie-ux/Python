#! /usr/bin/env python3
# Copyright (c) 2026 Luz

"""Directory: ex6/.

Files to Submit: ft_garden_analytics.py
Authorized: super(), print(), range(), round(), staticmethod(),
classmethod().
"""


class Plant:
    """Plant class composed of name, initial height and initial age."""

    def __init__(self, name: str, height: float, age: int, mod: float) -> None:

        self._name: str = name.capitalize()
        self._height: float = height
        self._age: int = age
        self._mod: float = mod
        self._stats: Plant.Statistics = Plant.Statistics()

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._stats.count_show()

    def grow(self) -> None:
        self._height += self._mod
        self._stats.count_grow()

    def aging(self) -> None:
        self._age += 1
        self._stats.count_age()

    def get_name(self) -> str:
        return self._name

    def ret_stats(self) -> None:
        return self._stats.print_stats()

    @staticmethod
    def check_age(age: int) -> None:
        """Check if a certain age is older than a year."""
        year: int = 365
        print(f"Is {age} days more than a year? -> {age > year}")

    @classmethod
    def anonymous(cls) -> Plant:
        """Create an unknown type of object."""
        return cls("Unknown plant", 0.0, 0, 0.0)

    class Statistics:
        """Statistics subclass of Plant."""

        def __init__(self) -> None:
            self.grow: int = 0
            self.age: int = 0
            self.show: int = 0

        def count_grow(self) -> None:
            self.grow += 1

        def count_age(self) -> None:
            self.age += 1

        def count_show(self) -> None:
            self.show += 1

        def print_stats(self) -> None:
            print(f"Stats: {self.grow} grow, {self.age} age, {self.show} show")


class Flower(Plant):
    """Child Class of Plant."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        mod: float,
        color: str,
    ) -> None:
        super().__init__(name, height, age, mod)
        self._color: str = color
        self._bloom: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

    def has_bloomed(self) -> None:
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def grow_bloom(self) -> None:
        if not self._bloom:
            self._bloom = True
            print(f"[asking the {self._name.lower()} to grow and bloom]")
            self.grow()
            self.has_bloomed()


class Seed(Flower):
    """Child Class of Plant."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        mod: float,
        color: str,
    ) -> None:
        super().__init__(name, height, age, mod, color)
        self._seeds: int = 0

    def show(self) -> None:
        super().show()
        self.has_bloomed()
        print(f"Seeds: {self._seeds}")

    def age_grow_bloom(self) -> None:
        if not self._bloom:
            self._bloom = True
            for _i in range(20):
                self.grow()
                self.aging()
            self._seeds = 42
            print(f"[make the {self._name.lower()} grow, age and bloom]")


class Tree(Plant):
    """Child Class of Plant."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        mod: float,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age, mod)
        self._diameter: float = trunk_diameter
        self._shade: int = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._diameter}cm")
        display(self)
        print(f"{self._shade} shade ")
        self.produce_shade()
        self._shade += 1

    def produce_shade(self) -> None:
        """Asks the Tree to produce a shade."""
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}cm", end=" ")
        print(f"long and {self._diameter}cm wide.")

    def get_shade(self) -> int:
        return self._shade


def display(plant: Plant) -> None:
    """Display Plant statistics."""
    print(f"[statistics for {plant.get_name()}]")
    plant.ret_stats()


def ft_garden_analytics() -> None:
    """Print the plants types statistics."""
    print("=== Garden Analytics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print("\n=== Flower")
    flower: Flower = Flower("rose", 15.0, 10, 8.0, "red")
    flower.show()
    flower.has_bloomed()
    display(flower)
    flower.grow_bloom()
    flower.show()
    display(flower)
    print("\n=== Tree")
    tree: Tree = Tree("oak", 200.00, 365, 10, 5.0)
    tree.show()
    display(tree)
    print(f"{tree.get_shade()} shade ")
    print("\n=== Seed")
    seed: Seed = Seed("sunflower", 80.0, 45, 1.5, "yellow")
    seed.show()
    seed.age_grow_bloom()
    seed.show()
    display(seed)
    print("\n=== Anonymous")
    anon: Plant = Plant.anonymous()
    anon.show()
    display(anon)


def main() -> None:
    """TODO: describe main.

    TODO: add description.
    """
    ft_garden_analytics()


if __name__ == "__main__":
    main()
