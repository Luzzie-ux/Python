#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: data_processor.py
Authorized: builtins, standard types, import typing, import abc
"""

from typing import Any
from abc import ABC, abstractmethod
from sys import stdout, stdin, stderr

class DataProcessor(ABC):
    # validate, which will check whether the input data are appropriate for the current data processor. 
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    # ingest, which will process the input data. Each specialized class will need to override these methods.
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # output, which will output ingested data.
    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            x: int
            x = int(data)
            return x
        except ValueError as e:
            print(f"{e.__class__.__name__}: {e}")

    def ingest(self, data: Any) -> None:
        pass

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if int(data):
                return False
        except ValueError as e:
            print(f"{e.__class__.__name__}: {e}")

    def ingest(self, data: Any) -> None:
        pass

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if not data:
                return False
        except ValueError as e:
            print(f"{e.__class__.__name__}: {e}")

    def ingest(self, data: Any) -> None:
        pass


def data_processor() -> None:
    stdout.write("=== Code Nexus - Data Processor ===\n\n")
    return


def main() -> None:
    data_processor()
    return


if __name__ == "__main__":
    main()
