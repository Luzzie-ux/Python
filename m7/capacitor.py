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

from typing import Any
from ex0 import CreatureFactory
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)


def test_capabilities(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    creatures: list[Any] = [factory.create_base(), factory.create_evolved()]
    for creature in creatures:
        if creature._name == "Bloomelle" or creature._name == "Morphagon":
            print(" evolved:")
        else:
            print(" base:")
        print(f"{creature.describe()}\n" f"{creature.attack()}")
    print()


def main() -> None:
    factories = [HealingCreatureFactory(), TransformCreatureFactory()]
    for factory in factories:
        test_capabilities(factory)
    return


if __name__ == "__main__":
    main()
