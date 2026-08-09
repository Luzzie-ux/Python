#!/usr/bin/env python3

"""
ft_custom_errors.py
"""


class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def ft_plant_error() -> None:
    pe: str = "The tomato plant is wilting!"
    raise PlantError(pe)


def ft_water_error() -> None:
    we: str = "Not enough water in the tank!"
    raise WaterError(we)


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    for i in range(2):
        try:
            if i == 0:
                ft_plant_error()
            elif i == 1:
                ft_water_error()
        except (PlantError, WaterError) as e:
            print(f"Testing {e.__class__.__name__}...")
            print(f"Caught {e.__class__.__name__}: {e}\n")
    print("Testing catching all garden errors...")
    errors = [
        ft_plant_error,
        ft_water_error,
    ]
    for error in errors:
        try:
            error()
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


def main() -> None:
    ft_custom_errors()


if __name__ == "__main__":
    main()
