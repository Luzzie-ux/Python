#!/usr/bin/env python3

"""
capacitor.py will:

Create a healing Creature factory.
    •Create the base, then the evolved Creature and make them:
    1) be described;
    2) attack;
    3) heal.

Create a transforming Creature factory.
    •Create the base, then the evolved Creature and make them:
    1) be described;
    2) attack;
    3) transform;
    4) attack again;
    5) revert.
"""

from typing import cast, Any
from ex1 import (
    HealCapability,
    TransformCapability,
    HealingCreatureFactory,
    TransformCreatureFactory,
)


def test_heal(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    creatures: list[Any] = [factory.create_base(), factory.create_evolved()]
    for creature in creatures:
        if creature._name == "Bloomelle":
            print(" evolved:")
        else:
            print(" base:")
        print(
            f"{creature.describe()}\n"
            f"{creature.attack()}\n"
            f"{cast(HealCapability, creature).heal(creature)}"
        )
    print()


def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    creatures: list[Any] = [factory.create_base(), factory.create_evolved()]
    for creature in creatures:
        if creature._name == "Morphagon":
            print(" evolved:")
        else:
            print(" base:")
        print(
            f"{creature.describe()}\n"
            f"{creature.attack()}\n"
            f"{cast(TransformCapability, creature).transform()}\n"
            f"{creature.attack()}\n"
            f"{creature.revert()}"
        )


def main() -> None:
    test_heal(HealingCreatureFactory())
    test_transform(TransformCreatureFactory())
    return


if __name__ == "__main__":
    main()
