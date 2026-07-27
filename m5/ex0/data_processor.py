#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: data_processor.py
Authorized: builtins, standard types, import typing, import abc
"""

from typing import Any
from abc import ABC, abstractmethod


# Data Processor Exception
class DPE(Exception):
    def __init__(self, message: str = "Unknown Processor Error") -> None:
        super().__init__(message)


# Numeric Processor Exception
class NPE(DPE):
    def __init__(
        self, message: str = "Unknown Numeric Processor Error"
    ) -> None:
        super().__init__(message)


# Textual Processor Exception
class TPE(DPE):
    def __init__(self, message: str = "Unknown Text Processor Error") -> None:
        super().__init__(message)


# Logical Processor Exception
class LPE(DPE):
    def __init__(
        self, message: str = "Unknown Logical Processor Error"
    ) -> None:
        super().__init__(message)


# Original Data Construct
class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
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

    @abstractmethod
    def all_data(self, data: Any) -> bool:
        pass


# Numbers and List of Numbers
class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        elif isinstance(data, list):
            return self.all_data(data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data) is not True:
            raise NPE("Improper numeric data")
        items: list[int | float] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, str(item)))
            self._rank += 1

    def all_data(self, data: list[int | float]) -> bool:
        if not data:
            return False
        for i in data:
            if not isinstance(i, (int, float)):
                return False
        return True


# Strings and List of strings
class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return self.all_data(data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) is not True:
            raise TPE("Improper textual data")
        items: list[str] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1

    def all_data(self, data: list[str]) -> bool:
        if not data:
            return False
        for s in data:
            if not isinstance(s, str):
                return False
        return True


# Dictionaries and List of dicts
class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for d in data:
                return self.all_data(d)
        return self.all_data(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data) is not True:
            raise LPE("Improper logical error")
        items: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )
        for item in items:
            self._storage.append(
                (self._rank, f"{item['log_level']}: {item['log_message']}")
            )
            self._rank += 1

    # check if all the instances is a dict and inside that dict is two strs
    def all_data(self, data: dict[str, str]) -> bool:
        if not data:
            return False
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) and not isinstance(value, str):
                    return False
            return True
        return False


def test_validate(proc: DataProcessor) -> None:
    s: str = "Hello"
    i: int = 42
    d: dict[str, str] = {s: str(i)}
    print(f"\nTesting {proc.__class__.__name__}...")
    print(f" Trying to validate input '{i}': {proc.validate(i)}")
    print(f" Trying to validate input '{s}': {proc.validate(s)}")
    print(f" Trying to validate input '{d}': {proc.validate(d)}")
    return


def test_ingest(proc: DataProcessor) -> None:
    print("Testing invalid ingestion of data type 'None' ")
    proc.ingest(None)
    return


# will take, list of ints, strs, and dicts
def process(data: list[Any], proc: DataProcessor) -> None:
    print(f"\nProcessing {proc.__class__.__name__} data: {data}")
    proc.ingest(data)
    if isinstance(proc, NumericProcessor):
        print(" Extracting 3 values...")
        for _ in range(3):
            n_rank, n_value = proc.output()
            print(f" Numeric value {n_rank}: {n_value}")
    elif isinstance(proc, TextProcessor):
        print(" Extracting 1 value...")
        for _ in range(1):
            t_rank, t_value = proc.output()
            print(f" Numeric value {t_rank}: {t_value}")
    elif isinstance(proc, LogProcessor):
        print(" Extracting 2 values...")
        for _ in range(2):
            l_rank, l_value = proc.output()
            print(f" Numeric value {l_rank}: {l_value}")
    else:
        raise DPE("No Data Processor Match for Unknown Data Type")
    return


def data_processor() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    nproc: DataProcessor = NumericProcessor()
    tproc: DataProcessor = TextProcessor()
    lproc: DataProcessor = LogProcessor()
    procs: list[DataProcessor] = [nproc, tproc, lproc]
    datas: list[list[Any]] = [
        [1, 2, 3, 4, 5],
        ["Hello", "Nexus", "World"],
        [
            {"log_level": "NOTICE", "log_message": "Connection to server"},
            {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
        ],
    ]
    for proc in procs:
        test_validate(proc)
        try:
            test_ingest(proc)
        except DPE as e:
            print(f" Got exception: {e}")

    for data, proc in zip(datas, procs):
        process(data, proc)

    return


if __name__ == "__main__":
    data_processor()
