#!/usr/bin/env python3


"""
Directory: ex4/
Files to Submit: decorator_mastery.py
Authorized: functools.wraps, staticmethod
"""

from collections.abc import Callable
from functools import wraps
from time import sleep, time
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        name = getattr(func, "__name__", repr(func))
        print(f"Casting {name}...")
        start = time()
        f = func(*args, **kwargs)
        rest = time() - start
        print(f"Spell completed in {rest:.3f} seconds")
        return f

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = args[-1]
            if value >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying..."
                        f"(attempt {i}/{max_attempts})"
                    )
                    continue
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name}: with {power} power"


@spell_timer
def fireball(power: int) -> str:
    sleep(5.0)
    if power < 10:
        return "It needs more power!"
    return "Fireball cast!"


@retry_spell(3)
def test_spell(name: str) -> str:
    int(name)
    return f"{name} spell!"


def main() -> None:
    test_powers = [23, 11, 10, 7]
    spell_names = ["lightning", "earthquake", "meteor", "heal"]
    mage_names = ["Morgan", "Ember", "River", "Phoenix", "Ash", "Sage"]
    invalid_names = ["Jo", "A", "Alex123", "Test@Name"]

    print("Testing spell timer...")
    print(f"Result: {fireball(10)}")

    print("\nTesting retrying spell...")
    print(test_spell("Firestorm"))
    print(test_spell("42"))

    mage = MageGuild()
    print("\nTesting power validator...")
    for spell, power in zip(spell_names, test_powers, strict=False):
        print(mage.cast_spell(spell, power))
    print("\nTesting MageGuild..")
    for valid, invalid in zip(mage_names, invalid_names, strict=False):
        print(valid, end=": ")
        print(mage.validate_mage_name(valid))
        print(invalid, end=": ")
        print(mage.validate_mage_name(invalid))
    print()


if __name__ == "__main__":
    main()
