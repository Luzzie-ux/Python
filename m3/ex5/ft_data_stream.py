#!/usr/bin/env python3


"""
Directory: ex5/
Files to Submit: ft_data_stream.py
Authorized: next(), range(), len(), print(), import typing,
typing.Generator, import random, random.*
"""

import random
import typing

ACTIONS: list[str] = ["eat", "sleep", "run", "move", "grab", "climb", "swim"]

PLAYERS: list[str] = [
    "Alice",
    "Bob",
    "Charlie",
    "Dylan",
]


def gen_events() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(PLAYERS), random.choice(ACTIONS)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event: tuple[str, str] = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen: typing.Generator[tuple[str, str], None, None] = gen_events()
    for i in range(0, 1000):
        event: tuple[str, str] = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    events: list[tuple[str, str]] = []
    for _i in range(0, 10):
        events.append(next(gen))
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list {events}")
    return


if __name__ == "__main__":
    main()
