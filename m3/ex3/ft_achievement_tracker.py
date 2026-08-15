#!/usr/bin/env python3


"""Directory: ex3/.

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
    "First come, First serve",
]


def gen_player_achievements() -> set[str]:
    return set(random.sample(ACHIEVEMENTS, random.randint(3, 9)))


def main() -> None:
    all_achivements: set[str] = set(ACHIEVEMENTS)
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    print()
    distinct: set[str] = set()
    for achievements in players.values():
        distinct &= achievements
    print(f"\nAll distinct achievements: {distinct}")
    common: set[str] = all_achivements.copy()
    for achievements in players.values():
        common -= achievements
    print(f"\nCommon achievements: {common}\n")
    for player, achievements in players.items():
        other: set[str] = set()
        for o_player, o_achievements in players.items():
            if player != o_player:
                other |= o_achievements
        print(f"Only {player} has: {other - achievements}")
    print()
    missing: set[str] = set()
    for user, achievements in players.items():
        missing = all_achivements - achievements
        print(f"{user} is missing: {missing}")


if __name__ == "__main__":
    main()
