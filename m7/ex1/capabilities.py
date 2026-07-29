#!/usr/bin/env python3


"""
capabilities.py has:

A HealCapability abstract class that defines:
    the heal abstract method that takes a “target” parameter.

A TransformCapability abstract class that defines:
    the transform and revert abstract methods.

An attribute is used to make the state persistent
    and it impacts the attack implementation of Creature
    with this capability.

These methods will return simple strings that describe
    the action (just like the attack method).
"""

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str: ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._state: bool = False

    @abstractmethod
    def transform(self) -> str: ...

    @abstractmethod
    def revert(self) -> str: ...
