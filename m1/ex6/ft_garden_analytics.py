#!/usr/bin/env python3

"""
ft_garden_analytics.py
"""


class Plant():
    def __init__(self, name: str, height: float, age: int, mod: float) -> None:
        self._name: str = name.capitalize()
        self._height: float = 0
        self._age: int = 0
        self._mod: float = 0
        self.set_att(round(height, 2), age, round(mod, 2))
        self._stats: Plant.Stats = Plant.Stats()

    def grow(self) -> None:
        self._height = round(self._height + self._mod, 2)
        self._stats.count_grow()
        return

    def aging(self) -> None:
        self._age = self._age + 1
        self._stats.count_age()
        return

    def set_att(self, height: float, age: int, mod: float) -> None:
        if height < 0:
            print(f"{self._name}: Error: Height can't be negative")
            print("Height update Rejected")
        if age < 0:
            print(f"{self._name}: Error: Age can't be negative")
            print("Age update Rejected")
        if mod < 0:
            print(f"{self._name}: Error: Modifier can't be negative")
            print("Modifier update Rejected")
        else:
            self._height = height
            self._age = age
            self._mod = mod
        return

    def update(self, height: float, age: int) -> None:
        self.set_att(height, age, self._mod)
        if self._height == height:
            print(f"Height updated: {height}cm")
        if self._age == age:
            print(f"Age updated: {age} days")
        return

    def show(self) -> None:
        self._stats.count_show()
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    @staticmethod
    def check(age: int) -> None:
        print(f"Is {age} days more than a year? -> {age > 365}")

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    class Stats():
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def count_grow(self) -> None:
            self._grow_calls += 1

        def count_age(self) -> None:
            self._age_calls += 1

        def count_show(self) -> None:
            self._show_calls += 1

        def print_display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age,"
                  f" {self._show_calls} show")


class Flower(Plant):
    def __init__(self, name: str, age: int, height: float, mod: float,
                 color: str, isBloom: bool = False) -> None:
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


class Tree(Plant):
    def __init__(self, name: str, age: int, height: float, mod: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age, mod)
        self._diameter: float = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._diameter}cm")
        self.produce_shade()

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}cm", end=" ")
        print(f"long and {self._diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, age: int, height: float, mod: float,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age, mod)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self, days: int) -> None:
        for i in range(0, days):
            super().grow()
            self._nutritional_value += 1
            i += 1
        print(f"[make {self._name} grow and age for {days} days]")
        self.show()
