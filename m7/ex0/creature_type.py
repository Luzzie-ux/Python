#!/usr/bin/env python3


"""
creature_type.py has:

The following concrete classes that inherit from Creature:
        Flameling and Pyrodon, Aquabub, and Torragon,

Their attack method will return an appropriate string message.
"""

from .creature import Creature

class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire", "Ember")

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"


class Pyrogon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrogon", "Fire/Flying", "Flamethrower")

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water", "Water Gun")

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water", "Hidro Pump")

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"
