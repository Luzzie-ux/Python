#!/usr/bin/env python3


"""
Directory: ex2/
Files to Submit: data_pipeline.py
Authorized: builtins, standard types, import typing, import abc
"""

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def validation(self) -> None:
        pass

    @abstractmethod
    def ingest(self) -> None:
        pass


class NumericProcessor(DataProcessor):
    pass

class TextProcessor(DataProcessor):
    pass

class LogProcessor(DataProcessor):
    pass


def data_pipeline() -> None:
    print("=== Code Nexus - Data Processor ===")
    return


def main() -> None:
    data_pipeline()
    return


if __name__ == "__main__":
    main()
