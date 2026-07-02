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


def gen_player_achievements() -> set[str]:
    achv: list[str] = random.sample(ACHIEVEMENTS, random.randint(2, 7))
    return set(achv)


def ft_achievement_tracker() -> None:
    all_achv: set[str] = set(ACHIEVEMENTS)
    print("=== Achievement Tracker System ===")
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    com: set[str] = set.union(alice, bob, charlie, dylan)
    inter: set[str] = set.intersection(alice, bob, charlie, dylan)
    print(f"\nAll distinct achievements: {com}")
    print(f"\nCommon achievements: {inter}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print()
    print(f"Alice doesnt have: {all_achv.difference(alice)}")
    print(f"Bob doesnt have: {all_achv.difference(bob)}")
    print(f"Charlie doesnt have: {all_achv.difference(charlie)}")
    print(f"Dylan doesnt have: {all_achv.difference(dylan)}")

    return


def main() -> None:
    ft_achievement_tracker()


if __name__ == "__main__":
    main()
