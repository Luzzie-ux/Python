#!/usr/bin/env python3


"""
scope_mysteries.py
"""

from collections.abc import Callable
from typing import TYPE_CHECKING, Any


def mage_counter() -> Callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> Callable:
    accumulator = initial_power

    def accumulated(amount: Any) -> int:
        nonlocal accumulator
        accumulator += amount
        return accumulator

    return accumulated


def enchantment_factory(enchantment_type: str) -> Callable:
    def concatenate(item_name: str) -> str:
        return enchantment_type + " " + item_name

    return concatenate


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: Any, value: Any) -> None:
        storage[key] = value

    def recall(key: Any) -> Any:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    initial_powers = [65, 60, 63]
    power_additions = [9, 20, 12]
    enchantment_types = ["Radiant", "Shocking", "Frozen"]
    items_to_enchant = ["Shield", "Amulet", "Ring", "Wand"]

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    for power in initial_powers:
        accumulator = spell_accumulator(power)
        for addition in power_additions:
            print(f"Base {power} add {addition}: {accumulator(addition)}")

    print("\nTesting enchantment factory...")

    print("\nTesting memory vault...")


if __name__ == "__main__":
    main()
