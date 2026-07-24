#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: data_processor.py
Authorized: builtins, standard types, import typing, import abc
"""

from typing import Any
from abc import ABC, abstractmethod
from sys import stdout, stderr


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items: list[int | float] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, str(item)))
            self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (str)) for x in data)
        return False

    
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper textual data")
        items: list[str] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(key, dict)
                and all(
                    isinstance(i, str) and isinstance(j, str)
                    for i, j in key.items()
                )
                for key in data
            )
        return isinstance(data, dict) and all(
            isinstance(i, str) and isinstance(j, str)
            for i, j in data.items()
        ) 

    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise ValueError("Improper logical error")
        items: list[dict] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(
                (self._rank, f"{item['log_level']}: {item['log_message']}")
            )
            self._rank += 1


def data_processor() -> None:
    stdout.write("=== Code Nexus - Data Processor ===\n\n")
    s: str = "Hello"

    n1: DataProcessor = NumericProcessor()
    stdout.write("Testing Numeric Processor...\n")
    stdout.write(f" Trying to validate input: '42': {n1.validate(42)}\n")
    stdout.write(
        f" Trying to validate input: '{s}': {n1.validate(s)}\n"
    )

    stdout.write(
        " Test invalid ingestion of string 'foo' without prior validation\n"
    )
    try:
        n1.ingest("foo")
    except ValueError as n_e:
        stderr.write(f" Got exception: {n_e}\n")

    data_n: list[int | float] = [1, 2, 3, 4, 5]
    stdout.write(f" Processing data: {data_n}\n")
    n1.ingest(data_n)
    stdout.write(" Extracting 3 values...\n")
    for _ in range(3):
        n_rank, n_value = n1.output()
        stdout.write(f" Numeric value {n_rank}: {n_value}\n")

    t1: DataProcessor = TextProcessor()
    stdout.write("\nTesting Text Processor...\n")
    stdout.write(f" Trying to validate input '42': {t1.validate(42)}\n")

    stdout.write(" Test invalid ingestion of number 4 without prior validation\n")
    try:
        t1.ingest(4)
    except ValueError as t_e:
        stderr.write(f" Got exception: {t_e}\n")
    
    data_t: list[str] = ['Hello', 'Nexus', 'World']
    stdout.write(f" Processing data: {data_t}\n")
    t1.ingest(data_t)
    stdout.write(" Extracting 1 value...\n")
    t_rank, t_value = t1.output()
    stdout.write(f" Text value {t_rank}: {t_value}\n")

    l1: DataProcessor = LogProcessor()
    stdout.write("\nTesting Log Processor...\n")
    stdout.write(f" Trying to validate string '{s}': {l1.validate(s)}\n")

    stdout.write(" Test invalid ingestion of an item without prior validation\n")
    try:
        l1.ingest(67)
    except ValueError as l_e:
        stderr.write(f" Got exception: {l_e} \n")

    data_l: list[dict] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'}, 
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    stdout.write(f" Processing data: {data_l} \n")
    l1.ingest(data_l)
    stdout.write(" Extracting 2 values...\n")
    for _ in range(2):
        rank, value = l1.output()
        stdout.write(f" Log entry {rank}: {value}\n")
    return


def main() -> None:
    data_processor()
    return


if __name__ == "__main__":
    main()
