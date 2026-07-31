#!/usr/bin/env python3

"""
creatures.py
"""

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from .capabilities import PoisonCapability, DarkCapability


class Snape(Creature, PoisonCapability, HealCapability):
    def __init__(self) -> None:
        HealCapability.__init__(self)
        PoisonCapability.__init__(self, 1.0)
        Creature.__init__(self, "Snape", "Poison", "Grime Rain", 20, 40)
        self._heal: float = self._hp * (self._mp / 100)
        self._poison_points += int(self._poison_points * self._modifier)

    def attack(self) -> str:
        return f"{self._name} casts {self._attack}!\n{self.poison(self)}"

    def heal(self, target: Creature) -> str:
        heal: int = int(self._heal)
        return f"{target._name} heals itself for a small amount ({heal})"

    def poison(self, target: Creature) -> str:
        turns: int = self._poison_points
        if target._name == self._name:
            return f"{target._name} is now buffed for {turns} turns"
        return f"{target._name} is now poisoned for {turns} turns"


class Viper(Creature, PoisonCapability, HealCapability):
    def __init__(self) -> None:
        HealCapability.__init__(self)
        PoisonCapability.__init__(self, 1.5)
        Creature.__init__(
            self, "Viper", "Poison/Thunder", "Karmic Thunderstorm", 35, 50
        )
        self._heal: float = self._hp * (self._mp / 50)
        self._poison_points += int(self._poison_points * self._modifier)

    def attack(self) -> str:
        return f"{self._name} summons {self._attack}!\n{self.poison(self)}"

    def heal(self, target: Creature) -> str:
        heal: int = int(self._heal)
        return f"{target._name} heals itself for a large amount ({heal})"

    def poison(self, target: Creature) -> str:
        turns: int = self._poison_points
        if target._name == self._name:
            return f"{target._name} is now buffed for {turns} turns"
        return f"{target._name} is now poisoned for {turns} turns"


class Veilaw(Creature, DarkCapability, TransformCapability):
    def __init__(self) -> None:
        TransformCapability.__init__(self)
        DarkCapability.__init__(self, 1.2)
        Creature.__init__(self, "Veilaw", "Dark", "Talon Strike")
        self._evade *= self._mod

    def attack(self) -> str:
        if not self._state:
            return f"{self._name} uses {self._attack}!"
        shadow_strike: str = self.still_image()
        return f"{shadow_strike}\n{self._name} uses shadow strike!"

    def transform(self) -> str:
        if not self._state:
            self._state = True
            return f"{self._name} shifts into a sharper form!"
        return f"[{self._name} is already on its best form]"

    def revert(self) -> str:
        self._state = False
        return f"{self._name} returns to normal."

    def still_image(self) -> str:
        self._evade *= 2.5
        return f"{self._name} hides in the shadows"


class Umbralon(Creature, DarkCapability, TransformCapability):
    def __init__(self) -> None:
        TransformCapability.__init__(self)
        DarkCapability.__init__(self, 1.8)
        Creature.__init__(
            self, "Umbralon", "Dark/Explosive", "Boom Claw", evade=12
        )
        self._evade *= self._mod

    def attack(self) -> str:
        if not self._state:
            return f"{self._name} uses {self._attack}!"
        clones: str = (
            f"{self.still_image()}\n"
            f"{self._name} and its clones use {self._attack}")
        return clones

    def transform(self) -> str:
        if not self._state:
            self._state = True
            return f"{self._name} morphs into a volcanic monster!"
        return f"[{self._name} is already on its best form]"

    def revert(self) -> str:
        self._state = False
        return f"{self._name} stabelizes its form."

    def still_image(self) -> str:
        self._evade *= 5.0
        return f"{self._name} casts shadow clones"
