#!/usr/bin/env python3


"""
Directory: ex5/
Files to Submit: ft_data_stream.py
Authorized: next(), range(), len(), print(), import typing,
typing.Generator, import random, random.*
"""

import typing
import random

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
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


def con_event(
    lista: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(lista) > 0:
        event: tuple[str, str] = random.choice(lista)
        lista.remove(event)
        yield event


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    stream: typing.Generator[tuple[str, str], None, None] = gen_event()
    name: str
    move: str
    for i in range(1000):
        name, move = next(stream)
        print(f"Event {i}: Player {name} did action {move}")
    events: list[tuple[str,str]] = []
    for i in range(0, 10):
        events.append(next(stream))
    print(f"Built list of 10 events: {events}")
    for event in con_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")
    return


def main() -> None:
    ft_data_stream()
    return


if __name__ == "__main__":
    main()
