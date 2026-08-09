#!/usr/bin/env python3

"""
tournament.py
"""

from typing import List, Tuple

from ex0 import AquaFactory as AF
from ex0 import CreatureFactory as CF
from ex0 import FlameFactory as FF
from ex0.creature import Creature
from ex1 import HealingCreatureFactory as HCF
from ex1 import TransformCreatureFactory as TCF
from ex2 import (
    AggressiveStrategy as AS,
)
from ex2 import (
    BattleStrategy as BS,
)
from ex2 import (
    DarkFactory as DF,
)
from ex2 import (
    DefensiveStrategy as DS,
)
from ex2 import (
    InvalidActError as IAE,
)
from ex2 import (
    NormalStrategy as NS,
)
from ex2 import (
    PoisonFactory as PF,
)

Opponent = Tuple[CF, BS]


def battle(ops: List[Opponent]) -> None:
    size: int = len(ops)
    print(f"*** Tournament ***\n{size} opponents involved")
    for i in range(0, size):
        for j in range(i + 1, size):
            a = ops[i]
            b = ops[j]
            f1, s1 = a
            f2, s2 = b
            factories: list[CF] = [f1, f2]
            c1: Creature = factories[0].create_base()
            c2: Creature = factories[1].create_base()
            print(
                "\n   * BATTLE *\n"
                f" {c1.describe()}\n"
                "   vs."
                f"\n {c2.describe()}\n\n"
                "NOW FIGHT!\n"
            )
            for line in s1.act(c1):
                print(line)
            for line in s2.act(c2):
                print(line)
    return


def format_tournament(tournament: list[Opponent]) -> str:
    parts: list[str] = []
    for o in tournament:
        f, s = o
        beast: Creature = f.create_base()
        mode: str = type(s).__name__
        parts.append(f"({beast._name}+{mode.removesuffix('Strategy')})")
    return " [ " + ", ".join(parts) + " ]"


def main() -> None:
    tournament: list[list[Opponent]] = [
        [(FF(), NS()), (HCF(), DS())],
        [(FF(), AS()), (HCF(), DS())],
        [(AF(), NS()), (HCF(), DS()), (TCF(), AS())],
        [(FF(), NS()), (AF(), NS()), (PF(), DS()), (DF(), AS())],
    ]
    j: int = 0
    for i in range(1, len(tournament) + 1):
        print(f"=== Tournament {i} ===")
        try:
            print(f"{format_tournament(tournament[j])}")
            battle(tournament[j])
        except IAE as e:
            print(f"Battle error, aborting tournament: {e}")
        finally:
            j += 1
    return


if __name__ == "__main__":
    main()
