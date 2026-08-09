#!/usr/bin/env python3

"""
capabilities.py
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ex0.creature import Creature


class PoisonCapability(ABC):
    def __init__(self, mod: float = 0.5) -> None:
        super().__init__()
        self._poison_points: int = 3
        self._modifier: float = mod

    @abstractmethod
    def poison(self, target: Creature) -> str: ...


class DarkCapability(ABC):
    def __init__(self, mod: float = 0.5) -> None:
        super().__init__()
        self._ability: float = 10.0
        self._mod: float = mod

    @abstractmethod
    def still_image(self) -> str: ...
