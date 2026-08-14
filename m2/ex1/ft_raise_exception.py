#!/usr/bin/env python3

"""
Directory: ex1/
Files to Submit: ft_raise_exception.py
Authorized: int(), print()
"""


def input_temperature(temp_str: str) -> int:
    """
    Input_temperature now will raise an ValueError
    if the value stored in var temp is higher than
    40 or lower than 0
    """
    temp: int = int(temp_str)
    hot: int = 40
    cold: int = 0
    if temp > hot:
        too_hot: str = f"{temp}°C is too hot for plants (max 40°C)"
        raise ValueError(too_hot)
    if temp < cold:
        too_cold: str = f"{temp}°C is too cold for plants (min 0°C)"
        raise ValueError(too_cold)
    return temp


def test_temperature(inputs: list[str]) -> None:
    """
    Tests the return value of input_temperature(),
    if it fails, it will not crash the program,
    but print to stdout the msg:
    Caught input_temperatue error: {e}
    where e stores ValueError
    """
    for inputx in inputs:
        try:
            print(f"Input data is {inputx}")
            temp: int = input_temperature(inputx)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


def ft_raise_exception() -> None:
    print("=== Garden Temperature Checker ===")
    inputs: list[str] = ["25", "abc", "100", "-50"]
    test_temperature(inputs)


def main() -> None:
    ft_raise_exception()


if __name__ == "__main__":
    main()
