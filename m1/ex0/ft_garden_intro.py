#!/usr/bin/env python3
# Copyright (c) 2026 Luz

"""Directory: ex0/.

Files to Submit: ft_garden_intro.py
Authorized: print()
"""


def ft_garden_intro() -> None:
    """Print garden info."""
    print("=== Welcome to My Garden ===")
    name: str = "Rose"
    print(f"Plant: {name}")
    height: float = 25
    print(f"Height: {height} cm")
    age: int = 30
    print(f"Age: {age} days")
    print()
    print("=== End of Program ===")


def main() -> None:
    """Entry point."""
    ft_garden_intro()


if __name__ == "__main__":
    main()
