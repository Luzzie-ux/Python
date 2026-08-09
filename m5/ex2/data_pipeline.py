#!/usr/bin/env python3


"""
Directory: ex2/
Files to Submit: data_pipeline.py
Authorized: builtins, standard types, import typing, import abc
"""

import math
from abc import ABC, abstractmethod
from typing import Any, Protocol


# Data Processor Exception
class DataProcessorError(Exception):
    def __init__(self, message: str = "Processor Error") -> None:
        super().__init__(message)


# Numeric Processor Exception
class NumericProcessorError(DataProcessorError):
    def __init__(
        self,
        message: str = "Improper numeric error",
    ) -> None:
        super().__init__(message)


# Textual Processor Exception
class TextualProcessorError(DataProcessorError):
    def __init__(self, message: str = "Improper textual error") -> None:
        super().__init__(message)


# Logical Processor Exception
class LogProcessorError(DataProcessorError):
    def __init__(
        self,
        message: str = "Improper logical error",
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
        if isinstance(data, list):
            return self.ft_all(data)
        return False

    def ingest(self, data: float | list[int | float]) -> None:
        if self.validate(data) is not True:
            raise NumericProcessorError
        items: list[int | float] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, str(item)))
            self._rank += 1

    # check for ints or floats inside list
    def ft_all(self, data: list[int | float]) -> bool:
        if not data:
            return False
        return all(isinstance(i, (int, float)) for i in data)


# Strings and List of strings
class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return self.ft_all(data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) is not True:
            raise TextualProcessorError
        items: list[str] = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1

    # check for instances of str inside list
    def ft_all(self, data: list[str]) -> bool:
        if not data:
            return False
        return all(isinstance(s, str) for s in data)


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
            raise LogProcessorError
        items: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )
        for item in items:
            self._storage.append(
                (self._rank, f"{item['log_level']}: {item['log_message']}"),
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


# defines the base structure through duck typing for future classes
#  such as CSVEP and JSONEP
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None: ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv: list[str] = [s for _, s in data]
        print(f"CSV Output:\n {','.join(csv)}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json: list[str] = [f'"item_{n}": "{s}"' for n, s in data]
        print(f"JSON Output:\n {{{', '.join(json)}}}")


class DataStream:
    def __init__(self) -> None:
        self._procs: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._procs.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for proc in self._procs:
            for i in range(len(stream) - 1, -1, -1):
                item: Any = stream[i]
                if proc.validate(item) is not True:
                    print(
                        "DataStream Error - "
                        f"Can't process element in stream: {item}",
                    )
                    continue
                proc.ingest(item)
                del stream[i]
        self.print_processors_stats()

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._procs:
            n: int = min(nb, len(proc._storage))
            data: list[tuple[int, str]] = [proc.output() for _ in range(n)]
            plugin.process_output(data)


def data_pipeline() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    data: list[Any] = [
        "Hello world",
        [math.pi, -1, math.e],
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
    batch: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    stream: DataStream = DataStream()
    procs: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    print("Initialize Data Stream...")
    stream.process_stream(data)
    print()
    print("Registering Processors...\n")
    for proc in procs:
        stream.register_processor(proc)
    print(f"Send first batch of data on stream: {data}")
    try:
        stream.process_stream(data)
    except DataProcessorError as e:
        print(f" Got exception: {e}")
    print("Send 3 processed data from each processor to a CSV plugin")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()
    print(f"Send another batch of data: {batch}")
    try:
        stream.process_stream(batch)
    except DataProcessorError as e:
        print(f" Got exception: {e}")
    print("Send 3 processed data from each processor to a JSON plugin")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    data_pipeline()
