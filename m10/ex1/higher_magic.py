#!/usr/bin/env python3


"""
Directory: ex1/
Files to Submit: higher_magic.py
Authorized: callable(), Callable
"""

from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball takes {power} HP from {target}"


def condition(target: str, power: int) -> bool:
    del target
    if not power < 10:
        return True
    return False


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return res1, res2

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, multiplier * power)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condicional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return condicional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence


def main() -> None:
    test_values = [25, 15, 6, 67]
    test_targets = ["Dragon", "Goblin", "Wizard", "Knight"]

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined(test_targets[0], test_values[0])
    print(f"{result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball(test_targets[1], test_values[1]))

    print("\nTesting conditional caster...")
    conditional_spell = conditional_caster(condition, heal)
    print(conditional_spell(test_targets[2], test_values[2]))
    print(conditional_spell(test_targets[2], test_values[3]))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([heal, fireball, condition])
    print(sequence(test_targets[3], test_values[3]))


if __name__ == "__main__":
    main()
