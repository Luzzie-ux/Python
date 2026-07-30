#!/usr/bin/env python3


"""
creature.py has:

A Creature abstract class that holds attributes for the name
and the type of the Creature, an abstract method attack
and a concrete generic method describe that will return a standard message
using the name and the type of the Creature.
"""

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(
        self,
        name: str,
        type: str,
        attack: str,
        hp: int = 50,
        mp: int = 20,
        evade: float = 25.0,
    ) -> None:
        super().__init__()
        self._name: str = name
        self._type: str = type
        self._attack: str = attack
        self._hp: int = hp
        self._mp: int = mp
        self._evade: float = evade

    @abstractmethod
    def attack(self) -> str: ...

    def describe(self) -> str:
        return f"{self._name}: is a {self._type} type Creature"
