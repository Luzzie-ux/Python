#!/usr/bin/env python3


"""
Directory: ex1/
Files to Submit: loading.py, requirements.txt, pyproject.toml
Authorized: pandas, requests, matplotlib, numpy, sys, importlib
"""

import sys
from importlib import import_module as imp

dependencies: list[str] = (
    "pandas",
    "numpy",
    "matplotlib"
)


def check() -> list:
    print("Checking dependencies:")
    pkgs = []
    for mod in dependencies:
        try:
            pkgs.append(imp(mod))
        except ImportError as e:
            print(f"{e}")
            continue
    if not pkgs:
        conflict()
    comparisons(pkgs)
    
        

def conflict() -> None:
    print("\nERROR: Required packages are missing.\n")
    print("To install with pip:")
    print("    pip install -r requirements.txt")
    print("    python loading.py")
    print("\nTo install with Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py")
    sys.exit(1)


def comparisons(pkgs: list) -> None:
    i: int = 0
    for pkg in pkgs:
        version: str | None = getattr(pkg, "__version__", "unknown")
        print(f"{pkg.__name__}: ", end="")
        print(f"({version})")
        if pkg.__name__ == dependencies[i]:
            if i == 0:
                matrix()
            elif i == 1:
                resolve()
            elif i == 2:
                save()
            else:
                break
        i += 1
    print(
        "\ndependency manager comparison:\n"
        "pip: do it yourself :c\n"
        "but its 5 bytes\n"
        "\n"
        "poetry: does it for you :D\n"
        "tho its like 500 billion GB"
    )


def matrix() -> None: ...


def resolve() -> None: ...


def save() -> None: ...


def main() -> None:
    print("LOADING STATUS: Loading programs... \n")
    check()
    return


if __name__ == "__main__":
    main()
