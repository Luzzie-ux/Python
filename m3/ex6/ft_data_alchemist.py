#!/usr/bin/env python3


"""Directory: ex6/.

Files to Submit: ft_data_alchemist.py
Authorized: import random, random.*, print(), len(), sum(), round(
"""

import random

PLAYERS: list[str] = [
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


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    print(f"Intial list of players: {PLAYERS}\n")
    upper: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all the names capitalized: {upper}")
    caps: list[str] = [name for name in PLAYERS if name[0].isupper()]
    print(f"New list of capitalized names only: {caps}\n")
    score: dict[str, int] = {key: random.randint(0, 5000) for key in upper}
    print(f"Score dict: {score}\n")
    ave: float = sum(score.values()) / len(score.keys())
    print(f"Score average: {round(ave, 2)}")
    high: dict[str, int] = {key: p for key, p in score.items() if p > ave}
    print(f"High score: {high}")


if __name__ == "__main__":
    main()
