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
    print(f"*** Tournament ***\n{len(ops)} opponents involved")
    print("\n   * BATTLE *\n")
    return


def format_tournament(tournament: list[Opponent]) -> str:
    parts: list[str] = []
    for o in tournament:
        f, s = o
        beast = f.create_base()
        name: str = type(s).__name__
        parts.append(f"({beast._name}+{name.removesuffix('Strategy')})")
    return " [ " + ", ".join(parts) + " ]"


def main() -> None:
    Tournament: list[list[Opponent]] = [
        [(FF(), NS()), (HCF(), DS())],
        [(FF(), AS()),(HCF(), AS())],
        [(AF(), NS()),(HCF(), DS()),(TCF(), AS())]
    ]
    j: int = 0
    k: int = 0
    for i in range(1, 4):
        print(f"=== Tournament {i} ===")
        try:
            print(f"{format_tournament(Tournament[j])}")
            battle(Tournament[j])
        except IAE as e:
            print(f"Battle error, aborting tournament: {e}")
        finally:
            j += 1; k += 1
    return


if __name__ == "__main__":
    main()
