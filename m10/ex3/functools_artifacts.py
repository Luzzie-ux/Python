#!/usr/bin/env python3


"""
Directory: ex3/
Files to Submit: functools_artifacts.py
Authorized: functools, operator
"""

import operator
from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    match operation:
        case "add":
            return reduce(operator.add, spells)
        case "multiply":
            return reduce(operator.mul, spells)
        case "max":
            return max(spells)
        case "min":
            return min(spells)
        case _:
            print("Operation not supported")
    return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n + 1) + memoized_fibonacci(n + 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return f"Unknown spell type: {spell}"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchatment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:
    spell_powers = [28, 25, 50, 40, 38, 40]
    operations = ["add", "multiply", "max", "min"]
    fibonacci_tests = [12, 19, 12]

    print("Testing spell reducer...")
    for op in operations:
        print(f"Operation {op}: {spell_reducer(spell_powers, op)}")
    print("\nTesting partial enchanter...")
    print("\nTesting memoized fibonacci...")
    for test in fibonacci_tests:
        print(f"Fib({test}): {memoized_fibonacci(test)}")
    print(memoized_fibonacci.cache_info())
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher((1, 2)))

    return


if __name__ == "__main__":
    main()
