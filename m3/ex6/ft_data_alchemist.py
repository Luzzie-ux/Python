#!/usr/bin/env python3


"""
Directory: ex6/
Files to Submit: ft_data_alchemist.py
Authorized: import random, random.*, print(), len(), sum(), round()
"""

import random


def ft_data_alchemist() -> None:
    mixed_list: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    all_cap_list: list[str] = [name.capitalize() for name in mixed_list]
    only_cap_list: list[str] = [
        name for name in mixed_list if name[0].isupper()
    ]
    scores: dict[str, int] = {
        name: random.randint(0, 1000) for name in all_cap_list
    }
    average: float = sum(scores.values()) / len(scores.keys())
    highs: dict[str, int] = {
        name: score for name, score in scores.items() if score > average
    }
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {mixed_list}")
    print(f"New list with all names capitalized: {all_cap_list}")
    print(f"New list of capitalized names only: {only_cap_list}")
    print(f"Score dict: {scores}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {highs}")


def main() -> None:
    ft_data_alchemist()
    return


if __name__ == "__main__":
    main()
