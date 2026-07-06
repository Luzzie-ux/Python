#!/usr/bin/env python3


"""
Directory: ex5/
Files to Submit: ft_data_stream.py
Authorized: next(), range(), len(), print(), import typing,
typing.Generator, import random, random.*
"""

import typing
import random


ACTIONS: list[str] = [
    "eat",
    "sleep",
    "run",
    "move",
    "grab",
    "climb",
    "swim"
]

PLAYERS: list[str] = [
    "Alice",
    "Bob",
    "Charlie",
    "Dylan",
]


def gen_events() -> typing.Generator[tuple[str,str], None, None]:
    while True:
        yield random.choice(PLAYERS), random.choice(ACTIONS)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    for i in range(0, 6):
        event: tuple[str,str] = next(gen_events())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    return


if __name__ == "__main__":
    main()


"""
$> python3 ft_data_stream.py
=== Game Data Stream Processor ===
Event 0: Player bob did action run
Event 1: Player alice did action eat
Event 2: Player bob did action sleep
Event 3: Player bob did action grab
Event 4: Player dylan did action run
Event 5: Player bob did action move
Built list of 10 events: [('charlie', 'move'), ('dylan', 'grab'), ('alice', 'use'), ('alice', 'use'), ('
charlie', 'swim'), ('bob', 'run'), ('charlie', 'move'), ('dylan', 'climb'), ('alice', 'use'), ('bob
', 'release')]
Got event from list: ('charlie', 'swim')
Remains in list: [('charlie', 'move'), ('dylan', 'grab'), ('alice', 'use'), ('alice', 'use'), ('bob', '
run'), ('charlie', 'move'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]
Got event from list: ('alice', 'use')
Remains in list: [('charlie', 'move'), ('dylan', 'grab'), ('alice', 'use'), ('bob', 'run'), ('charlie',
'move'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]
Got event from list: ('charlie', 'move')
Remains in list: [('dylan', 'grab'), ('alice', 'use'), ('bob', 'run'), ('charlie', 'move'), ('dylan', '
climb'), ('alice', 'use'), ('bob', 'release')]
Got event from list: ('charlie', 'move')
Remains in list: [('dylan', 'grab'), ('alice', 'use'), ('bob', 'run'), ('dylan', 'climb'), ('alice', '
use'), ('bob', 'release')]
Got event from list: ('alice', 'use')
Remains in list: [('dylan', 'grab'), ('bob', 'run'), ('dylan', 'climb'), ('alice', 'use'), ('bob', '
release')]
Got event from list: ('bob', 'release')
Remains in list: [('dylan', 'grab'), ('bob', 'run'), ('dylan', 'climb'), ('alice', 'use')]
Got event from list: ('bob', 'run')
Remains in list: [('dylan', 'grab'), ('dylan', 'climb'), ('alice', 'use')]
Got event from list: ('dylan', 'climb')
Remains in list: [('dylan', 'grab'), ('alice', 'use')]
Got event from list: ('alice', 'use')
Remains in list: [('dylan', 'grab')]
Got event from list: ('dylan', 'grab')
Remains in list: []
18

"""