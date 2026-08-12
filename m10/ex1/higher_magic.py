#!/usr/bin/env python3


"""
higher_magic.py
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable: ...


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable: ...


def conditional_caster(condition: Callable, spell: Callable) -> Callable: ...


def spell_sequence(spells: list[Callable]) -> Callable: ...


def main() -> None:
    return


if __name__ == "__main__":
    main()
