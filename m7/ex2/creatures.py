#!/usr/bin/env python3

"""
creatures.py
"""

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from .capabilities import AcidCapability, ShadowCapability


class Snape(Creature, AcidCapability, HealCapability):
    def __init__(self) -> None:
        HealCapability.__init__(self)
        AcidCapability.__init__(self, 1.0)
        Creature.__init__(self, "Snape", "Acid", "Grime Rain", 20, 40)
        self._heal: float = self._hp * (self._mp / 100)

    def attack(self) -> str:
        return f"{self._name} casts {self._attack}!"

    def poison(self, target: Creature) -> str:
        self._poison_points + (self._poison_points * self._modifier)
        turns: int = self._poison_points
        if target._name == self._name:
            return self.heal(target)
        return f"{target._name} is now poisoned for {turns} turns"

    def heal(self, target: Creature) -> str:
        heal: int = int(self._heal)
        return f"{target._name} heals itself for a small amount({heal})"


class Viper(Creature, AcidCapability, HealCapability):
    def __init__(self) -> None:
        HealCapability.__init__(self)
        AcidCapability.__init__(self, 1.5)
        Creature.__init__(
            self, "Viper", "Acid/Ghost", "Karmic Thunderstorm", 35, 50
        )
        self._heal: float = self._hp * (self._mp / 50)

    def attack(self) -> str:
        return f"{self._name} summons {self._attack}!"

    def poison(self, target: Creature) -> str:
        self._poison_points + (self._poison_points * self._modifier)
        turns: int = self._poison_points
        if target._name == self._name:
            return self.heal(target)
        return f"{target._name} is now poisoned for {turns} turns"

    def heal(self, target: Creature) -> str:
        heal: int = int(self._heal)
        return f"{target._name} heals itself for a large amount({heal})"


class ShadowBeast(Creature, ShadowCapability, TransformCapability):
    ...


class EvolvedShadowBeast(Creature, ShadowCapability, TransformCapability):
    ...
