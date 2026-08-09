# ex0/__init_.py

"""
Directory: ex0/
Files to Submit: battle.py, ex0/ as a package with all needed files in it
Authorized: builtins, standard types, import typing, import abc
"""

from .factory import CreatureFactory
from .factory_type import AquaFactory, FlameFactory

__all__: list[str] = [
    "AquaFactory",
    "CreatureFactory",
    "FlameFactory",
]
