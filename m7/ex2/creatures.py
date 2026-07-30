#!/usr/bin/env python3

"""
creatures.py
"""

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from .capabilities import AcidCapability, ShadowCapability


class Snape(Creature, AcidCapability, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Snape", "Acid", "Grime Rain", 20, 40)
        AcidCapability.__init__(self, 1.0)
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self._name} casts {self._attack}\n{self.poison(Creature)}!"

    def poison(self, target: Creature) -> str:
        self._poison_points + (self.self._poison_points * self._modifier)
        turns: int = self._poison_points
        if target._name == self._name:
            return self.heal(target)
        return f"{target._name} is now poisoned for {turns} turns"

    def heal(self, target: Creature) -> str:
        return f"{target._name} heals itself for a small amount"


class Viper(Creature, AcidCapability, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Viper", "Acid/Ghost", "Karma Storm", 35, 50)
        AcidCapability.__init__(self, 1.0)
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self._name} summons {self._attack}\n{self.poison(Creature)}!"

    def poison(self, target: Creature) -> str:
        self._poison_points + (self.self._poison_points * self._modifier)
        turns: int = self._poison_points
        if target._name == self._name:
            return self.heal(target)
        return f"{target._name} is now poisoned for {turns} turns"

    def heal(self, target: Creature) -> str:
        return f"{target._name} heals itself for a large amount"


class ShadowBeast(Creature, ShadowCapability): ...


class EvolvedShadowBeast(Creature, ShadowCapability): ...