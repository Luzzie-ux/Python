#!/usr/bin/env python3


"""
factory.py has:

A CreatureFactory abstract class that will allow you to create the base Crea-
ture and the evolved Creature for the same family, using the create_base and
create_evolved abstract methods
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .creature import Creature


class CreatureFactory(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._evolved: bool = False

    @abstractmethod
    def create_base(self) -> Creature: ...

    @abstractmethod
    def create_evolved(self) -> Creature: ...
