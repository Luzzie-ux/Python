#!/usr/bin/env python3


"""
ft_distillation_0.py
"""

from alchemy.potions import strength_potion, healing_potion


def main() -> None:
    print("=== Distilation 0 ===")
    print("Direct Access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")
    return


if __name__ == "__main__":
    main()
