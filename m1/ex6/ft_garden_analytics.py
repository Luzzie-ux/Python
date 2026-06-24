#! /usr/bin/env python3

"""
ft_garden_analytics.py
"""


class Plant:
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

    @staticmethod
    def check_age(age: int) -> None:
        """
        Static method of Plant used to check
        if a certain age is older than a year
        """
        print(f"Is {age} days more than a year? -> {age > 365}")

    @classmethod
    def anonymous(cls) -> "Plant":
        """
        Class method of Plant used to create an unknown type of object
        """
        return cls("Unknown plant", 0.0, 0, 0.0)

    class Statistics:
        """
        Statistics subclass of Plant, used to count how many times the methods:
        grow, age and show are used by each child of Plant
        """

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
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        mod: float,
        color: str,
        isBloom: bool = False,
    ) -> None:
        super().__init__(name, height, age, mod)
        self._color: str = color
        self._isBloom: bool = isBloom

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

    def has_bloomed(self) -> None:
        if self._isBloom:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def grow_bloom(self) -> None:
        if not self._isBloom:
            self._isBloom = True
            print(f"[asking the {self._name.lower()} to grow and bloom]")
            self.grow()
            self.has_bloomed()


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, mod: float, color: str
    ) -> None:
        super().__init__(name, height, age, mod, color)
        self._seeds: int = 0

    def show(self) -> None:
        super().show()
        self.has_bloomed()
        print(f"Seeds: {self._seeds}")

    def age_grow_bloom(self) -> None:
        if not self._isBloom:
            self._isBloom = True
            for i in range(20):
                self.grow()
                self.aging()
            self._seeds = 42
            print(f"[make the {self._name.lower()} grow, age and bloom]")


class Tree(Plant):
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
        """
        Asks the Tree to produce a shade
        """
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}cm", end=" ")
        print(f"long and {self._diameter}cm wide.")


def display(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.print_stats()


def ft_garden_analytics() -> None:
    """Prints the plants types statistics"""
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
    print(f"{tree._shade} shade ")
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
    pass


if __name__ == "__main__":
    ft_garden_analytics()
