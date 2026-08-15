#!/usr/bin/env python3


"""Directory: ex2/.

Files to Submit: scope_mysteries.py
Authorized: nonlocal
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def mage_counter() -> Callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> Callable:
    accumulator = initial_power

    def accumulated(amount: int) -> int:
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

    def store(key: int, value: str) -> None:
        storage[key] = value

    def recall(key: int) -> str:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    initial_powers = [65, 60, 63]
    power_additions = [9, 20, 12]
    enchantment_types = ["Radiant", "Shocking", "Frozen", "Arcane"]
    items_to_enchant = ["Shield", "Amulet", "Ring", "Wand"]

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    for addition, power in zip(power_additions, initial_powers, strict=False):
        accumulator = spell_accumulator(power)
        print(f"Base {power} add {addition}: {accumulator(addition)}")

    print("\nTesting enchantment factory...")
    for item, enchantment in zip(
        items_to_enchant, enchantment_types, strict=False
    ):
        factory = enchantment_factory(enchantment)
        print(factory(item))

    print("\nTesting memory vault...")
    vault = memory_vault()
    for i, item in zip(range(5), items_to_enchant, strict=False):
        vault["store"](i, item)
    for i in range(5):
        print(f"{i}: {vault['recall'](i)}")


if __name__ == "__main__":
    main()
