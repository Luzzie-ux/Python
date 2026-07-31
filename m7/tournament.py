#!/usr/bin/env python3

"""
tournament.py
"""

from typing import List, Tuple
from ex0 import AquaFactory as AF, CreatureFactory as CF, FlameFactory as FF
from ex0.creature import Creature
from ex1 import HealingCreatureFactory as HCF, TransformCreatureFactory as TCF
from ex2 import (
    AggressiveStrategy as AS,
    PoisonFactory as PF,
    BattleStrategy as BS,
    DarkFactory as DF,
    DefensiveStrategy as DS,
    InvalidActError as IAE,
    NormalStrategy as NS,
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
    Tournament: list[list[Opponent]] = [
        [(FF(), NS()), (HCF(), DS())],
        [(FF(), AS()), (HCF(), DS())],
        [(AF(), NS()), (HCF(), DS()), (TCF(), AS())],
        [(FF(), NS()), (AF(), NS()), (PF(), DS()), (DF(), AS())],
    ]
    j: int = 0
    for i in range(1, len(Tournament) + 1):
        print(f"=== Tournament {i} ===")
        try:
            print(f"{format_tournament(Tournament[j])}")
            battle(Tournament[j])
        except IAE as e:
            print(f"Battle error, aborting tournament: {e}")
        finally:
            j += 1
    return


if __name__ == "__main__":
    main()
