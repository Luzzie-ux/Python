# seed inventory

"""
defines function that prints seed inventory taken from stdin
"""


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """
    function that displays seed inventory with inputs from stdin
    """
    if unit.lower() == "packets":
        print(f"{seed_type.capitalize()} seeds: "
              f"{quantity} {unit.lower()} avaiable")
    elif unit.lower() == "grams":
        print(f"{seed_type.capitalize()} seeds: "
              f"{quantity} {unit.lower()} total")
    elif unit.lower() == "area":
        print(f"{seed_type.capitalize()} seeds: "
              f"covers {quantity} square meters")
    else:
        print("Unknown unit type")
    return


def main() -> None:
    type: str = str(input("Choose a seed type: "))
    quantity: int = int(input("Choose a qunatity: "))
    unit: str = str(input("Choose a unit: "))
    ft_seed_inventory(type, quantity, unit)


if __name__ == "__main__":
    main()
