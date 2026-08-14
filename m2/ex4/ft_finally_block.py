#!/usr/bin/env python3

"""
Directory: ex4/
Files to Submit: ft_finally_block.py
Authorized: print(), str.capitalize()
"""


class PlantError(Exception):
    def __init__(self, message: str = "Error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        msg: str = f"Watering {plant_name}: [OK]"
        return print(msg)
    plant_errmsg: str = f"Invalid plant name to water: '{plant_name}'"
    raise PlantError(plant_errmsg)


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
            "\nCleanup always happens, even with errors!",
        )


def ft_finally_block() -> None:
    print("=== Garden Watering System ===")
    test_watering_plant()


def main() -> None:
    ft_finally_block()


if __name__ == "__main__":
    main()
