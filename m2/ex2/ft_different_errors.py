#!/usr/bin/env python3
# Copyright (c) 2026 Luz

"""Directory: ex2/.

Files to Submit: ft_different_errors.py
Authorized: print(), open(), int().
"""


def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            10 / 0  # noqa: B018
        case 2:
            open("/non/existent/file", encoding="utf-8")
        case 3:
            "good morning" + 1  # noqa: B018    #ty: ignore
        case _:
            operation_number * 10


def test_error_types() -> None:
    ops: list[int] = [0, 1, 2, 3, 4]
    for op in ops:
        try:
            print(f"Testing operation {op}...")
            garden_operations(op)
            print("Operation completed successfully")
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError,
        ) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("\nAll error types tested successfully")


def ft_different_errors() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()


def main() -> None:
    ft_different_errors()


if __name__ == "__main__":
    main()
