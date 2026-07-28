#!/usr/bin/env python3


"""
ft_alembic_5.py
"""

from alchemy import create_air


def main() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing the create_air: {create_air()}")
    return


if __name__ == "__main__":
    main()
