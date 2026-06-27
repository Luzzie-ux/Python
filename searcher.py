#!/usr/bin/env python3


"""
Searching implementation in python
"""

from sys import argv
from pathlib import Path


def help() -> None:
    print(
        "usage: ./searcher [option] ... [file]\n"
        "Version: 1.0.0 \n"
        "Options:\n"
        " --help:                       Displays this information.\n"
        " --file [file]:                Displays the contents of [file(s)] in the terminal\n"
        " --find [str]...:              Prints the number of occurrences of [str] in [file(s)]\n"
        " --replace [old][new]...:      Replaces one string for a new one\n"
        "\n"
        "[nothing here yet]\n"
    )
    return


def read_file(str_to_find: str, file: str) -> int:
    count: int = 0
    with open(file, "r") as f:
        line: str = f.readline()
        while line:
            count += line.lower().count(str_to_find.lower())
            line = f.readline()
    return count


def replace_str(target_str: str, new_str: str, file: str) -> None:
    filedata: str
    with open(file, 'r') as f:
        filedata = f.read()
    filedata = filedata.replace(target_str, new_str)
    with open(file, "w") as f:
        f.write(filedata)
    return


def parser(args: list[str]) -> None:
    if args[0] == "--help":
        return help()
    elif args[0] == "--file":
        for file in args[1:]:
            f = Path(file)
            if f.exists():
                with open(file, "r") as fd:
                    print(f"{fd.read()}\n")
            else:
                return print(f"Could not find file {file}")
        return
    elif args[0] == "--find":
        for file in args[2:]:
            f = Path(file)
            if f.exists():
                occurences: int = read_file(args[1], file)
                print(f"{occurences} occurrences of: '{args[1]}' in {file}")
            else:
                return print(f"Could not find file {file}")
        return
    elif args[0] == "--replace":
        for file in args[3:]:
            f = Path(file)
            if f.exists():
                replace_str(args[1], args[2], file)
            else:
                return print(f"Could not find file {file}")


def main() -> None:
    if len(argv) < 2:
        return
    try:
        parser(argv[1:])
    except (Exception, IndexError) as e:
        print(f"{e.__class__.__name__}: {e}")
    return


if __name__ == "__main__":
    main()
