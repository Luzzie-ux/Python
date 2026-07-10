#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: data_processor.py
Authorized: builtins, standard types, import typing, import abc
"""

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.data: list[str] = []

    @abstractmethod
    def validation(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self, data: Any) -> None:
        return

class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validation(self, number: int) -> None:
        return super().validation()
    
    def ingest(self, array: list[int]) -> None:
        return super().ingest()

class TextProcessor(DataProcessor):
    pass

class LogProcessor(DataProcessor):
    pass


def data_processor() -> None:
    print("=== Code Nexus - Data Processor ===")
    return


def main() -> None:
    data_processor()
    return


if __name__ == "__main__":
    main()
