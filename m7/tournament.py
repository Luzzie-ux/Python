#!/usr/bin/env python3

"""
tournament.py
"""

from typing import List, Tuple, Any
from ex0 import AquaFactory as AF, CreatureFactory as CF, FlameFactory as FF
from ex1 import HealingCreatureFactory as HCF, TransformCreatureFactory as TCF
from ex2 import (
    AggressiveStrategy as AS,
    BattleStrategy as BS,
    DefensiveStrategy as DS,
    IAE,
    NormalStrategy as NS,
)


Opponent = Tuple[CF, BS]


def battle(ops: List[Opponent]) -> None:
    size: int = len(ops)
    print(f"*** Tournament ***\n{size} opponents involved")
    print("\n   * BATTLE *\n")
    for i in range(size):
        a = ops[i]; b = ops[i + 1 % size]
        f1, s1 = a
        f2, s2 = b
        b1 = f1.create_base()
        b2 = f2.create_base()

    return
        

def format_tournament(tournament: list[Opponent]) -> str:
    parts: list[str] = []
    for o in tournament:
        f, s = o
        beast = f.create_base()
        mode: str = type(s).__name__
        parts.append(f"({beast._name}+{mode.removesuffix('Strategy')})")
    return " [ " + ", ".join(parts) + " ]"


def main() -> None:
    Tournament: list[list[Opponent]] = [
        [(FF(), NS()), (HCF(), DS())],
        [(FF(), AS()),(HCF(), AS())],
        [(AF(), NS()),(HCF(), DS()),(TCF(), AS())]
    ]
    j: int = 0
    for i in range(1, len(Tournament)):
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
