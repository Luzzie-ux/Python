#!/usr/bin/env python3


"""
ft_distillation_0.py
"""

from alchemy.potions import strength_potion, healing_potion


def main() -> None:
    print("=== Distillation 0 ===\n"
          "Direct access to alchemy/potions.py\n"
          f"Testing strength_potion: {healing_potion()}\n"
          f"Testing heal alias: {strength_potion()}")
    return


if __name__ == "__main__":
    main()
