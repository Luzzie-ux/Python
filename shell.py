#!/usr/bin/env python3


"""
Shell implementation in python
"""

from sys import argv
from pathlib import Path


def help() -> None:
    print(
        "usage: ./shell [option] ... [file]\n"
        "Version: 2.0.0 \n"
        "Options:\n"
        " --help:                       Displays this information.\n"
        " --display [file]:             Displays the contents of [file(s)] in"
        " the terminal\n"
        " --search    [str]...:         Prints the number of occurrences of "
        "[str] in [file(s)]\n"
        " --rename  [new_name]...:      Renames the [file(s)] given with a "
        "[new_name]\n"
        " --change [old][new]...:      Replaces one string for a [new] one\n"
        " --make-file [file]:           Makes new [file(s)] in current root "
        "if they dont exist yet\n"
        " --make-dir  [dir]:            Makes new [dir(s)] in current root "
        "if they dont exist yet\n"
    )
    return


def display_file(args: list[str]) -> None:
    for file in args:
        f = Path(file)
        if not f.exists():
            return print(f"Could not find file {file}")
        with open(file, "r") as fd:
            print(f"{fd.read()}\n")
    return


def read_file(args: list[str]) -> None:
    str_to_find: str = args[0]
    if not str_to_find.strip():
        return print(f"String {str_to_find} cannot be empty")
    for file in args[1:]:
        count: int = 0
        line: str
        fd = Path(file)
        if not fd.exists():
            return print(f"Could not find file {file}")
        with open(file, "r") as f:
            line = f.readline()
            while line:
                count += line.lower().count(str_to_find.lower())
                line = f.readline()
    return


def rename_file(args: list[str]) -> None:
    size: int = len(args)
    if size % 2 != 0:
        return print("Error: each file must have a paired new name")
    for i in range(0, size, 2):
        new_name: str
        file: str
        new_path: Path
        new_name = args[i]
        if not new_name.strip():
            return print("New name cannot be empty")
        file = args[i + 1]
        f = Path(file)
        if not f.exists():
            return print(f"Could not find file {file}")
        new_path = f.parent / new_name
        if not new_path.exists():
            f.rename(new_path)
            continue
        print(
            f"{new_path} already exists, are you sure "
            "you want to rename it? The file with the "
            "same name will be truncated\n"
        )
        check: str = input("[y/n]: ")
        if check == "y":
            f.rename(new_path)
        else:
            return print("Closing edit")
    return


def replace_str(args: list[str]) -> None:
    target: str = args[0]
    new: str = args[1]
    for file in args[2:]:
        filedata: str
        fd = Path(file)
        if not fd.exists():
            return print(f"Could not find file '{file}'")
        if not target or not new:
            empty: str = "target" if not target else "new"
            return print(f"{empty} string cannot be empty")
        with open(file, "r") as f:
            filedata = f.read()
        filedata = filedata.replace(target, new)
        with open(file, "w") as f:
            f.write(filedata)
    return


def create_file(files: list[str]) -> None:
    for file in files:
        f = Path(file)
        if f.exists():
            return print(f"'{file}' already exists")
        f.parent.mkdir(parents=True, exist_ok=True)
        f.touch()
    return


def create_directory(dirs: list[str]) -> None:
    for d_name in dirs:
        d = Path(d_name)
        if d.exists():
            return print(f"'{d_name}' already exists")
        d.mkdir(parents=True, exist_ok=True)
    return


def parser(args: list[str]) -> None:
    if args[0] == "--help":
        return help()
    elif args[0] == "--display":
        return display_file(args[1:])
    elif args[0] == "--search":
        return read_file(args[1:])
    elif args[0] == "--rename":
        return rename_file(args[1:])
    elif args[0] == "--change":
        return replace_str(args[1:])
    elif args[0] == "--make-file" or args[0] == "-mkf":
        return create_file(args[1:])
    elif args[0] == "--make-dir" or args[0] == "-mkd":
        return create_directory(args[1:])


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
