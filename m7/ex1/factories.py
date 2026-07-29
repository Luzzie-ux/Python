#!/usr/bin/env python3


"""
factories.py has:

The concrete classes HealingFactory, TransformFactory,
inheriting from CreatureFactory, that will handle the creation
of the base and evolved Creature for each family:
(Sproutling and Bloomelle for HealingFactory,
Shiftling and Morphagon for TransformFactory)
"""

from ex0.creature import Creature
from ex0.factory import CreatureFactory
from .creatures import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
