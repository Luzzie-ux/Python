#!/usr/bin/env python3

"""ft_transmutation_0.py."""

import alchemy.transmutation.recipes


def main() -> None:
    recipe: str = alchemy.transmutation.recipes.lead_to_gold()
    print("=== Transmutation 0 ===")
    print(
        "Using file alchemy/transmutation/recipes.py direcly\n"
        f"Testing lead to gold: {recipe}",
    )


if __name__ == "__main__":
    main()
