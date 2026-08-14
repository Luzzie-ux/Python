#! /usr/bin/env python3

"""
Directory: ex0/
Files to Submit: ft_first_exception.py
Authorized: int(), print()
"""


def input_temperature(temp_str: str) -> int:
    """Returns an integer from input"""
    return int(temp_str)


def test_temperature(inputs: list[str]) -> None:
    """
    Tests the return value of input_temperature(),
    if it fails, it will raise an error
    """
    for inputx in inputs:
        try:
            print(f"Input data is {inputx}")
            input_temperature(inputx)
            print(f"Temperature is now {inputx}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


def ft_first_exception() -> None:
    print("=== Garden Temperature ===\n")
    inputs: list[str] = ["25", "abc"]
    test_temperature(inputs)


def main() -> None:
    ft_first_exception()


if __name__ == "__main__":
    main()
