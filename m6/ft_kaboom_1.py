#!/usr/bin/env python3


"""
ft_kaboom_1.py
"""

print(
    "=== Kaboom 1 ===\n"
    "Access to alchemy/grimoire/dark_spellbook.py directly\n"
    "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION",
)


def main() -> None:
    import alchemy.grimoire.dark_spellbook as recorder

    print(f"{recorder.dark_spell_record('Fantasy', 'Earth, wind, and fire')}")


if __name__ == "__main__":
    main()
