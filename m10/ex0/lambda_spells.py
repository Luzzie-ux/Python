#!/usr/bin/env python3


"""
lambda_spells.py
"""

import typing
import collections.abc
import itertools
import functools
import operator


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]: ...


def spell_transformer(spells: list[str]) -> list[str]: ...


def mage_stats(mages: list[dict]) -> dict: ...


def main() -> None:
    artifacts = [
        {
           "name" :"Fire Staff",
           "power":92,
           "type":"Fire",
        },
        {
            "name":"Crystal Orb",
            "power":85,
            "type":"Crystal",
        },
    ]
    print(artifact_sorter(artifacts))
    return


if __name__ == "__main__":
    main()
