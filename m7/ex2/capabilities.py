#!/usr/bin/env python3

"""
capabilities.py
"""

from ex0.creature import Creature
from abc import ABC, abstractmethod


class AcidCapability(ABC):
    def __init__(self, mod: float = 0.5) -> None:
        super().__init__()
        self._poison_points: int = 3
        self._modifier: float = mod

    @abstractmethod
    def poison(self, target: Creature) -> str: ...


class ShadowCapability(ABC):
    def __init__(self, ability: float = 10.0, mod: float = 0.5) -> None:
        super().__init__()
        self._ability: float = ability
        self._mod: float = mod
