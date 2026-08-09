#!/usr/bin/env python3

"""
battle.py will test ex0 by:

Instantiating the Flameling and Aquabub factories.
 •Using a single function that receives a factory object
    and verifies that it can create the base and evolved Creature,
    and then each Creature can be described and can attack.
 •Using another function that receives both factories
    and makes base Creature fight.
"""

from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test(factory: CreatureFactory) -> None:
    print(f"Testing {factory.__class__.__name__}")
    creatures = [factory.create_base(), factory.create_evolved()]
    for creature in creatures:
        print(creature.describe())
        print(creature.attack())
    print()
    return


def battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    factories: list[CreatureFactory] = [f1, f2]
    for i in range(0, len(factories), 2):
        c1 = factories[i].create_base()
        c2 = factories[i + 1].create_base()
        print(
            "Testing battle: \n"
            f" {c1.describe()}\n    vs. \n {c2.describe()}\nFight!\n\n"
            f" {c1.attack()}\n"
            f" {c2.attack()}"
        )
    return


def main() -> None:
    factories: list[CreatureFactory] = [FlameFactory(), AquaFactory()]
    for factory in factories:
        test(factory)
    battle(factories[0], factories[1])
    return


if __name__ == "__main__":
    main()
