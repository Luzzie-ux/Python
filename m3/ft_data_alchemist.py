#!/usr/bin/env python3


"""
ft_data_alchemist.py
"""

import random


def create_dict(names: list[str]) -> dict[str, int]:
    ids: dict[str, int] = {}
    for name in names:
        i: int = random.randint(0, 1000)
        ids[name] = i
    return ids


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
    all_cap_list: list[str] = []
    only_cap_list: list[str] = []
    for name in mixed_list:
        if name[0].isupper():
            only_cap_list.append(name)
        all_cap_list.append(name.capitalize())
    scores: dict[str, int] = create_dict(all_cap_list)
    average: float = sum(scores.values()) / len(scores.keys())
    highs: dict[str, int] = {}
    for name, score in scores.items():
        if score > average:
            highs[name] = score
    print("=== Game Data ALchemist ===")
    print(f"Initial list of players: {mixed_list}")
    print(f"New list with all names capitalized {all_cap_list}")
    print(f"New list of capitalized names only: {only_cap_list}")
    print(f"Score dict: {scores}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {highs}")


def main() -> None:
    ft_data_alchemist()
    return


if __name__ == "__main__":
    main()
