#!/usr/bin/env python3

"""
ft_garden_intro.py
"""


def ft_garden_intro() -> None:
    """Prints garden info"""
    print("=== Welcome to My Garden ===")
    name: str = "Rose"
    print(f"Plant: {name}")
    height: float = 25
    print(f"Height: {height} cm")
    age: int = 30
    print(f"Age: {age} days")
    print()
    print("=== End of Program ===")
    return


if __name__ == "__main__":
    ft_garden_intro()
