#!/usr/bin/env python3

"""
factories.py
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ex0.creature import Creature

from ex0.factory import CreatureFactory

from .creatures import Snape, Umbralon, Veilaw, Viper


class PoisonFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Snape()

    def create_evolved(self) -> Creature:
        self._evolved = True
        return Viper()


class DarkFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> Creature:
        return Veilaw()

    def create_evolved(self) -> Creature:
        self._evolved = True
        return Umbralon()
