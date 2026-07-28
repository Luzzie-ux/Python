#!/usr/bin/env python3


"""
ft_alembic_4.py
"""

import alchemy


def main() -> None:
    a: str = alchemy.create_air()
    print("=== Alembic 4 ===")
    print("Acessiing the alchemy module using 'import alchemy'")
    print("Testing create_air:", end=" ")
    print(a)
    print(
        "Now show that not all functions can be reached\n"
        "This will raise an exception!"
    )
    print("Testing the hidden create_earth:", end=" ")
    try:
        alchemy.create_earth()  #type: ignore
    except AttributeError as e:
        print(f"{e.__class__.__name__}: {e}")
    return


if __name__ == "__main__":
    main()
