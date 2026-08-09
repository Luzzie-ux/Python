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

from typing import cast

from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)


def test_heal(f: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    creatures = [f.create_base(), f.create_evolved()]
    for creature in creatures:
        h = cast(HealCapability, creature)
        if creature._name == "Bloomelle":
            print(" evolved:")
        else:
            print(" base:")
        print(
            f"{creature.describe()}\n"
            f"{creature.attack()}\n"
            f"{h.heal(creature)}"
        )
    print()


def test_trans(f: TransformCreatureFactory) -> None:
    print("Testing Creature with transformation capability")
    creatures = [f.create_base(), f.create_evolved()]
    for creature in creatures:
        t = cast(TransformCapability, creature)
        if creature._name == "Bloomelle" or creature._name == "Morphagon":
            print(" evolved:")
        else:
            print(" base:")
        print(
            f"{creature.describe()}\n"
            f"{creature.attack()}\n"
            f"{t.transform()}\n"
            f"{creature.attack()}\n"
            f"{t.revert()}"
        )
    print()


def main() -> None:
    factories = [HealingCreatureFactory(), TransformCreatureFactory()]
    for factory in factories:
        if isinstance(factory, HealingCreatureFactory):
            test_heal(factory)
        elif isinstance(factory, TransformCreatureFactory):
            test_trans(factory)
    return


if __name__ == "__main__":
    main()
