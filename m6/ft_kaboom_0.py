#!/usr/bin/env python3


"""
ft_kaboom_0.py
"""

from alchemy import grimoire


def main() -> None:
    spell: str = "Fantasy"
    allowed: str = "Earth, wind and Fire"
    record: str = grimoire.light_spell_record(spell, allowed)
    print(
        "=== Kaboom 0 ===\n"
        "Using grimoirer module directly\n"
        "Testing record light spell: "
        f"{record}",
    )


if __name__ == "__main__":
    main()
