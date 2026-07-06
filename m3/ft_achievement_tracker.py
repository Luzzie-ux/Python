#!/usr/bin/env python3


"""
Directory: ex3/
Files to Submit: ft_achievement_tracker.py
Authorized: len(), print(), import random, random.*, set(), set.union(),
set.intersection(), set.difference()
"""

import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
    "Are We There Yet",
    "In The End Of The World",
    "Destroyer of Hearts",
    "First come, First serve"
]


def gen_player_achievements() -> set[str]:
    return set(random.sample(ACHIEVEMENTS, random.randint(3,9)))


def main() -> None:
    all: set[str] = set(ACHIEVEMENTS)
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    print()
    distinct: set[str] = []
    for achievements in players.values():
        distinct = set.union(distinct, achievements)
    print(f"\nAll distinct achievements: {distinct}")
    common: set[str] = all.copy()
    for achievements in players.values():
        common = set.intersection(common, achievements)
    print(f"\nCommon achievements: {common}\n")
    print(f"Only Alice has: {a - b - c - d}")
    print(f"Only Bob has: {b - a - c - d}")
    print(f"Only Charlie has: {c - b - a - d}")
    print(f"Only Dylan has: {d - b - c - a}\n")
    
    print(f"")
    return


if __name__ == "__main__":
    main()
