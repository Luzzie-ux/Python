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

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

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
            print(f"[asking the {self._name.lower()} to bloom]")
            self.show()
        else:
            print(f"{self._name} is blooming beautifully!")


def ft_garden_analytics() -> None:
    """Prints the plants types statistics"""
    print("=== Garden Analytics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    flower: Flower = Flower("rose", 15, 10, 0.5, "red")
    flower.show()
    pass


if __name__ == "__main__":
    ft_garden_analytics()
