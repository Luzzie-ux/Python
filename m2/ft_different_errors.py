#!/usr/bin/env python3

"""
ft_different_errors.py

=== Garden Error Types Demo ===
Testing operation 0...
Caught ValueError: invalid literal for int() with base 10: 'abc'
Testing operation 1...
Caught ZeroDivisionError: division by zero
Testing operation 2...
Caught FileNotFoundError: [Errno 2] No such file or directory:
'/non/existent/file'
Testing operation 3...
Caught TypeError: can only concatenate str (not "int") to str
Testing operation 4...
Operation completed successfully
All error types tested successfully

ValueError - when bad data is provided
 (like "abc" instead of a number to int())
•ZeroDivisionError - when you try to divide by zero
•FileNotFoundError - when you try to open a file that does not exist
 (and if it's not open, no need to close() it)
•TypeError - when you try to mix diferent types that cannot be mixed
 (did you try to add a string and a number?)
"""


def bar() -> None:
    pass


if __name__ == "__main__":
    bar()
