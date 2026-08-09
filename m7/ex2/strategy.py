#!/usr/bin/env python3

"""
strategy.py has:

BattleStrategy abstract class that defines:
    the act and is_valid abstract methods.

The is_valid method returns a bool if a Creature can use the strategy,
    and the act method will be called by the tournament script.

•Three concrete classes that inherit from BattleStrategy:

    ◦The NormalStrategy, suitable for any Creature,
    that will simply use the attack method during the tournament.

    ◦The AggressiveStrategy, suitable for Creature with transform,
    that will transform, attack, and revert during the tournament.

    ◦The DefensiveStrategy, suitable for Creature with healing,
    that will attack and then heal during the tournament.

•In case an invalid strategy-Creature combination is tested,
    the is_valid method returns False. If the act method is called
    with an invalid combination, a dedicated exception is raised
"""

from abc import ABC, abstractmethod
from typing import cast

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


# Invalid Act Error
class InvalidActError(Exception):
    def __init__(self, msg: str = "Unknown Act Error") -> None:
        super().__init__(msg)


class BattleStrategy(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def act(self, creature: Creature) -> list[str]: ...

    @abstractmethod
    def is_valid(self, c: Creature) -> bool: ...


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            errmsg: str = f"Invalid Creature '{creature._name}'"
            nem: str = f"{errmsg} for this normal strategy"
            raise InvalidActError(nem)
        return [creature.attack()]

    def is_valid(self, c: Creature) -> bool:
        return isinstance(c, Creature)


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            errmsg: str = f"Invalid Creature '{creature._name}'"
            aem: str = f"{errmsg} for this aggresive strategy"
            raise InvalidActError(aem)
        t: TransformCapability = cast("TransformCapability", creature)
        return [t.transform(), creature.attack(), t.revert()]

    def is_valid(self, c: Creature) -> bool:
        return isinstance(c, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            errmsg: str = f"Invalid Creature '{creature._name}'"
            dem: str = f"{errmsg} for this defensive strategy"
            raise InvalidActError(dem)
        h: HealCapability = cast("HealCapability", creature)
        return [creature.attack(), h.heal(creature)]

    def is_valid(self, c: Creature) -> bool:
        return isinstance(c, HealCapability)
