#!/usr/bin/env python3


"""
factory_type.py has:

The concrete classes FlameFactory, AquaFactory,
HealingCreatureFactory and TransformCreaturefactory
inheriting from CreatureFactory, that will handle the creation
of the base and evolved Creature for each family
(respectively Flameling and Pyrodon for FlameFactory,
Aquabub and Torragon for AquaFactory,
Sproutling and Bloomelle for HealingFactory,
Shiftling and Morphagon for TransformFactory)
"""

from ex0 import CreatureFactory
from .creature import Creature
from .creature_type import (
    Flameling,
    Pyrogon,
    Aquabub,
    Torragon,
    Sprountling,
    Bloomelle,
    Shiftling,
    Morphagon
)


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrogon()


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Sprountling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()