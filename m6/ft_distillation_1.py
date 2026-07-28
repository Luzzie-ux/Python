#!/usr/bin/env python3


"""
ft_distillation_1.py
"""

import alchemy


def main() -> None:
    """
    Using: 'import alchemy'structure to access potions
    Testing strength_potion: Strength potion brewed with 'Fire element created'and 'Water element created'
    Testing heal alias: Healing potion brewed with 'Earth element created'and 'Air element created'
    """
    print("=== Distilation 1 ===")
    print("Using 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")
    return


if __name__ == "__main__":
    main()
