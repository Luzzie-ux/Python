#!/usr/bin/env python3


"""
factory_type.py has:

The concrete classes FlameFactory, AquaFactory,
inheriting from CreatureFactory, that will handle the creation
of the base and evolved Creature for each family
(respectively Flameling and Pyrodon for FlameFactory,
Aquabub and Torragon for AquaFactory,)
"""

from .factory import CreatureFactory
from .creature import Creature
from .creature_type import (
    Flameling,
    Pyrogon,
    Aquabub,
    Torragon,
)


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        self._evolved = True
        return Pyrogon()


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        self._evolved = True
        return Torragon()
