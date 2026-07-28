#!/usr/bin/env python3


"""
ft_alembic_2.py
"""

import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Acessing alchemy/elements.py using: 'import ...' structure")
    print("Testing create_earth:", end=" ")
    s: str = alchemy.elements.create_earth()
    print(s)
    return


if __name__ == "__main__":
    main()
