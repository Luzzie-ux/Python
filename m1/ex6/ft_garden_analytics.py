#! /usr/bin/env python3

"""
ft_garden_analytics.py
"""


class Plant():
    def __init__(self, name: str, height: float, age: int, mod: float) -> None:
        self._name: str = name.capitalize()
        self._height: float = height
        self._age: int = age
        self._mod: float = mod
        self._stats: Plant.Statistics = Plant.Statistics()

    def show(self) -> None:
        self._stats.count_show()
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._mod, 2)
        self._stats.count_grow()
        return

    def aging(self) -> None:
        self._age += 1
        self._stats.count_age()
        return

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

    class Statistics():
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
    def __init__(self, name: str, height: float, age: int,
                 mod: float, color: str, isBloom: bool = False) -> None:
        super().__init__(name, height, age, mod)
        self._color: str = color
        self._isBloom: bool = isBloom

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        self.bloom()

    def bloom(self) -> None:
        if not self._isBloom:
            self._isBloom = True
            print(f"{self._name} has not bloomed yet")
            display(self)
            print(f"[asking the {self._name.lower()} to grow and bloom]")
            self.grow()
            self.show()
        else:
            print(f"{self._name} is blooming beautifully!")
            display(self)


class Seed(Plant):
    def __init__(self, name: str, height: float, age: int, mod: float) -> None:
        super().__init__(name, height, age, mod)
        pass


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
    flower: Flower = Flower("rose", 15, 10, 8.0, "red")
    flower.show()
    pass


if __name__ == "__main__":
    ft_garden_analytics()
