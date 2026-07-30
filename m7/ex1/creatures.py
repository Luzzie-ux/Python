#!/usr/bin/env python3


"""
creatures.py has:

The following concrete classes that inherit from:
    Creature, HealCapability and TransformCapability:
        Sproutling and Bloomelle, Shiftling and Morphagon.

Their attack method will return an appropriate string message.
"""

from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sprountling", "Grass", "Vine Whip")
        HealCapability.__init__(self)
        self._heal: float = self._hp * (self._mp / 100)

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"

    def heal(self, target: Creature) -> str:
        heal: int = int(self._heal)
        if target._name == self._name:
            return f"{self._name} heals itself for a small amount({heal})"
        return f"{self._name} heals {target._name} for a small amount({heal})"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy", "Petal Dance")
        HealCapability.__init__(self)
        self._heal: float = self._hp * (self._mp / 50)

    def attack(self) -> str:
        return f"{self._name} uses {self._attack}!"

    def heal(self, target: Creature) -> str:
        heal: int = int(self._heal)
        if target._name == self._name:
            spell: str = (
                f"{self._name} heals itself "
                f"and others for a large amount({heal})"
            )
            return spell
        return f"{self._name} heals {target._name} for a large amount({heal})"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal", "normally")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self._state:
            return f"{self._name} attacks {self._attack}."
        return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        if not self._state:
            self._state = True
            return f"{self._name} shifts into a sharper form!"
        return f"[{self._name} is already on its best form]"

    def revert(self) -> str:
        self._state = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon", "normally")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self._state:
            return f"{self._name} attacks {self._attack}."
        return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        if not self._state:
            self._state = True
            return f"{self._name} morphs into a dragonic battle form!"
        return f"[{self._name} is already on its best form]"

    def revert(self) -> str:
        self._state = False
        return f"{self._name} stabilizes its form."
