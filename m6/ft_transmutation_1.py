#!/usr/bin/env python3

"""ft_transmutation_1.py."""

from alchemy import transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print(
        "Import transmutation module directly\n"
        f"Testing lead to gold: {transmutation.lead_to_gold()}",
    )


if __name__ == "__main__":
    main()
