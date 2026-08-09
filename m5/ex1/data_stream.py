#!/usr/bin/env python3


"""
Directory: ex1/
Files to Submit: data_stream.py
Authorized: builtins, standard types, import typing, import abc
"""

from abc import ABC, abstractmethod
from typing import Any


# Data Processor Exception
class DataProcessorError(Exception):
    def __init__(self, message: str = "Unknown Processor Error") -> None:
        super().__init__(message)


# Numeric Processor Exception
class NumericProcessorError(DataProcessorError):
    def __init__(
        self, message: str = "Unknown Numeric Processor Error"
    ) -> None:
        super().__init__(message)


# Textual Processor Exception
class TextualProcessorError(DataProcessorError):
    def __init__(self, message: str = "Unknown Text Processor Error") -> None:
        super().__init__(message)


# Logical Processor Exception
class LogProcessorError(DataProcessorError):
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
    def validate(self, data: Any) -> bool: ...

    @abstractmethod
    def ingest(self, data: Any) -> None: ...

    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)

    @abstractmethod
    def ft_all(self, data: Any) -> bool: ...


# Numbers and List of Numbers
class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        elif isinstance(data, list):
            return self.ft_all(data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data) is not True:
            raise NumericProcessorError("Improper numeric data")
        items: list[int | float] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, str(item)))
            self._rank += 1

    # check for ints or floats inside list
    def ft_all(self, data: list[int | float]) -> bool:
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
            return self.ft_all(data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) is not True:
            raise TextualProcessorError("Improper textual data")
        items: list[str] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1

    # check for instances of str inside list
    def ft_all(self, data: list[str]) -> bool:
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
                return self.ft_all(d)
        return self.ft_all(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data) is not True:
            raise LogProcessorError("Improper logical error")
        items: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )
        for item in items:
            self._storage.append(
                (self._rank, f"{item['log_level']}: {item['log_message']}")
            )
            self._rank += 1

    # check if all the instances is a dict and inside that dict is two strs
    def ft_all(self, data: dict[str, str]) -> bool:
        if not data:
            return False
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) and not isinstance(value, str):
                    return False
            return True
        return False


class DataStream:
    def __init__(self) -> None:
        self._procs: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._procs.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for proc in self._procs:
            name: str = proc.__class__.__name__
            print(f"\nRegistering {name}...")
            for i in range(len(stream) - 1, -1, -1):
                item: Any = stream[i]
                if proc.validate(item) is not True:
                    print(
                        "DataStream Error - "
                        f"Can't process element in stream: {item}"
                    )
                    continue
                proc.ingest(item)
                del stream[i]
        self.print_processors_stats()
        return

    def print_processors_stats(self) -> None:
        if not self._procs:
            print("== DataStream statistics ==")
            print("No processor found, no data")
            return
        print()
        print("== DataStream statistics ==")
        for p in self._procs:
            name: str = p.__class__.__name__
            t: int = p._rank
            r: int = len(p._storage)
            print(f"{name}:", end=" ")
            print(f"total {t} items processed, remaining {r} on processor")
        print()
        return


def data_stream() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    ds: DataStream = DataStream()
    data: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print("Initialize Data Stream...")
    ds.process_stream(data)
    ps: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    for p in ps:
        ds.register_processor(p)
    try:
        ds.process_stream(data)
    except DataProcessorError as e:
        print(f" Got exception: {e}")
    print("Consuming one element from each data processor")
    for p in ps:
        p.output()
    ds.print_processors_stats()
    return


if __name__ == "__main__":
    data_stream()
