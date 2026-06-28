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
        " --display [file]:                Displays the contents of [file(s)] in the terminal\n"
        " --find [str]...:              Prints the number of occurrences of [str] in [file(s)]\n"
        " --rename [new_name]...:       Renames the [file(s)] given with a [new_name]\n"
        " --replace [old][new]...:      Replaces one string for a [new] one\n"
        "\n"
    )
    return


def read_file(str_to_find: str, file: str) -> int:
    count: int = 0
    if not str_to_find.strip():
        print("String to find cannot be empty")
        return count
    with open(file, "r") as f:
        line: str = f.readline()
        while line:
            count += line.lower().count(str_to_find.lower())
            line = f.readline()
    return count


def rename_file(args: list[str]) -> None:
    size: int = len(args)
    new_name: str
    file: str
    new_path: Path
    if size % 2 == 0:
        for i in range(0, size, 2):
            new_name = args[i]
            if not new_name.strip():
                return print("New name cannot be empty")
            file = args[i + 1]
            f = Path(file)
            if f.exists():
                new_path = f.parent / new_name
                if new_path.exists():
                    print(
                        f"{new_path} already exists, are you sure "
                        "you want to rename it? The file with the "
                        "same name will be truncated\n"
                    )
                    check: str = input("[y/n]: ")
                    if check == "y":
                        f.rename(new_path)
                    elif check == "n":
                        return print("Closing edit")
                    else:
                        return print("Invalid input, nothing done")
                else:
                    f.rename(new_path)
            else:
                return print(f"Could not find file {file}")
        return
    else:
        return print("Error: each file must have a paired new name")


def replace_str(target_str: str, new_str: str, file: str) -> None:
    filedata: str
    if not target_str or not new_str:
        empty: str = "target" if not target_str else "new"
        return print(f"{empty} string cannot be empty")
    with open(file, 'r') as f:
        filedata = f.read()
    filedata = filedata.replace(target_str, new_str)
    with open(file, "w") as f:
        f.write(filedata)
    return


def parser(args: list[str]) -> None:
    file: str
    if args[0] == "--help":
        return help()
    elif args[0] == "--display":
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
    elif args[0] == "--rename":
        file = args[2]
        f = Path(file)
        if f.exists():
            new_path: Path = f.parent / args[1]
            f.rename(new_path)
        else:
            return print(f"Could not find file {file}")
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
