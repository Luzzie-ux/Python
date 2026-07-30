#!/usr/bin/env python3

"""
factories.py
"""

from ex0.creature import Creature
from ex0.factory import CreatureFactory
from .creatures import *


class AcidFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self):
        return

    def create_evolved(self):
        self._evolved = True
        return super().create_evolved()


class ShadowFactory(CreatureFactory): ...
