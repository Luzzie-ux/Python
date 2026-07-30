#!/usr/bin/env python3

"""
factories.py
"""

from ex0.creature import Creature
from ex0.factory import CreatureFactory
from .creatures import Snape, Viper


class AcidFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Snape()

    def create_evolved(self) -> Creature:
        self._evolved = True
        return Viper()


class ShadowFactory(CreatureFactory):
    ...
