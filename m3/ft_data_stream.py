#!/usr/bin/env python3


"""
Directory: ex5/
Files to Submit: ft_data_stream.py
Authorized: next(), range(), len(), print(), import typing,
typing.Generator, import random, random.*
"""

import typing
import random


PLAYERS: list = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "use",
    "release",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(PLAYERS), random.choice(ACTIONS)


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    name: tuple[str]
    move: tuple[str]
    for i in range(6): #trocar pra 1000
        name, move = next(gen_event())
        print(f"Event {i}: Player {name} did action {move}")
    stream: list[tuple[tuple[str], tuple[str]]] = []
    for i in range(11):
        stream.extend(next(gen_event()))
    print(f"Built list of 10 events: {stream}")
    return


def main() -> None:
    ft_data_stream()
    return


if __name__ == "__main__":
    main()
