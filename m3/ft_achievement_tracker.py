#!/usr/bin/env python3

"""
Directory: ex3/
Files to Submit: ft_achievement_tracker.py
Authorized: len(), print(), import random, random.*, set(), set.union(),
set.intersection(), set.interference()
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


def gen_player_achievements() -> set:
    achx: list[str] = random.sample(ACHIEVEMENTS, random.randint(2, 7))
    return set(achx)


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    alice: set = gen_player_achievements()
    bob: set = gen_player_achievements()
    charlie: set = gen_player_achievements()
    dylan: set = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    inter: set = set.intersection(alice, bob, charlie, dylan)
    com: set = set.union(alice, bob, charlie, dylan)
    print(f"\nAll distinct achievements: {inter}")
    print(f"\nCommon achievements: {com}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print()
    print(f"Only Alice has: {alice.difference(ACHIEVEMENTS)}")
    print(f"Only Bob has: {bob.difference(ACHIEVEMENTS)}")
    print(f"Only Charlie has: {charlie.difference(ACHIEVEMENTS)}")
    print(f"Only Dylan has: {dylan.difference(ACHIEVEMENTS)}")

    return


if __name__ == "__main__":
    ft_achievement_tracker()
