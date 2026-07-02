#!/usr/bin/env python3

"""
ft_finally_block.py
"""


class PlantError(Exception):
    def __init__(self, message: str = "Error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        return print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_plant() -> None:
    print("\nTesting valid plants...")
    valid_plants: list[str] = ["Tomato", "Lettuce", "Carrots"]
    print("Opening watering systems")
    try:
        for valid in valid_plants:
            water_plant(valid)
    finally:
        print("Closing watering system")
    print("\nTesting Invalid plants...")
    print("Opening watering systems")
    invalid_plants: list[str] = ["Tomato", "lettuce", "Carrot"]
    try:
        for invalid in invalid_plants:
            water_plant(invalid)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        print(
            "Closing watering system\n"
            "\nCleanup always happens, even with errors!"
        )


def ft_finally_block() -> None:
    print("=== Garden Watering System ===")
    test_watering_plant()


def main() -> None:
    ft_finally_block()
    return


if __name__ == "__main__":
    main()
