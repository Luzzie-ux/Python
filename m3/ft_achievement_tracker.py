#!/usr/bin/env python3

"""
Directory: ex3/
Files to Submit: ft_achievement_tracker.py
Authorized: len(), print(), import random, random.*, set(), set.union(),
set.intersection(), set.difference()
"""

import random


ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Boss Slayer",
    "Speed Runner",
    "Untouchable",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Strategist",
    "Survivor",
    "Treasure Hunter",
    "Crafting Genius",
    "Sharp Mind",
    "Unstoppable",
    "Hidden Path Finder",
    "Dragon Slayer",
    "Legend",
]


def gen_player_achievements(n: int) -> set:
    achx: list[str] = random.sample(ACHIEVEMENTS, n)
    return set(achx)


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    alice: set = gen_player_achievements(random.randint(2, 9))
    bob: set = gen_player_achievements(random.randint(2, 9))
    charlie: set = gen_player_achievements(random.randint(2, 9))
    dylan: set = gen_player_achievements(random.randint(2, 9))
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    dif = set.difference(alice, bob, charlie, dylan)
    print(dif)

    return


if __name__ == "__main__":
    ft_achievement_tracker()
