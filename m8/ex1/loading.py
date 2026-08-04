#!/usr/bin/env python3


"""
Directory: ex1/
Files to Submit: loading.py, requirements.txt, pyproject.toml
Authorized: pandas, requests, matplotlib, numpy, sys, importlib
"""

import sys
from importlib import import_module as imp
from importlib.metadata import version, PackageNotFoundError as PNFE


def check() -> list:
    print("Checking dependencies:")
    Modules: list[str] = ["numpy", "pandas", "matplotlib"]
    size: int = len(Modules)
    pkgs = {}
    for name in Modules:
        try:
            pkgs[name] = imp(name)
        except (ImportError, PNFE) as e:
            print(f"[MISSING] {e}")
            continue
    if not pkgs or len(pkgs.values()) < size:
        conflict()
    for name in pkgs.keys():
        print(f"[OK] {name}: ", end="")
        print(f"({version(name)})", end="")
        print(f" - {desc(name)} ready")
    return compute()


def desc(name) -> str:
    match name:
        case "numpy":
            return "Numerical computation"
        case "pandas":
            return "Data manipulation"
        case "matplotlib":
            return "Visualization"
        case "requests":
            return "Network access "
        case _:
            return "No Description Yet but"


def conflict() -> None:
    print("\nERROR: Required packages are missing.\n")
    print("To install with pip:")
    print("    pip install -r requirements.txt")
    print("    python loading.py")
    print("\nTo install with Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py")
    sys.exit(1)


def compute() -> None:
    print("\nAnalyzing Matrix Data")
    import numpy as np

    s: int = 10
    t: int = 20

    rng = np.random.default_rng(42)
    pairs = rng.integers(1, s, size=(10, 2))

    matrix = np.zeros((s, t), dtype=np.int64)
    matrix[:, 0] = pairs[:, 0]
    matrix[:, 1] = pairs[:, 1]

    for col in range(2, t):
        matrix[:, col] = matrix[:, col - 1] + matrix[:, col - 2]
    return dataframe(matrix, s, t)


def dataframe(matrix, s, t) -> None:
    print("Processing 200 data points")
    import pandas as pd

    df = pd.DataFrame(
        matrix,
        index=[f"S{i}" for i in range(s)],
        columns=[f"T{i}" for i in range(t)],
    )
    return graph(df)


def graph(df) -> None:
    print("Generating visualization\n")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    for seq_label in df.index:
        ax.plot(df.columns, df.loc[seq_label], label=seq_label)

    ax.set_yscale("log")
    ax.set_title("Fibonacci-like Sequences")
    ax.set_xlabel("Term index")
    ax.set_ylabel("Value")
    ax.legend()

    return save(plt)


def save(plt) -> None:
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def manager() -> None:
    print(
        "\nDependency Manager Comparison:\n"
        "pip: do it yourself :c\n"
        "but its 5 bytes\n"
        "\n"
        "poetry: does it for you :D\n"
        "tho its like 500 Billion TB"
    )


def main() -> None:
    print("\nLOADING STATUS: Loading programs... \n")
    check()
    manager()
    return


if __name__ == "__main__":
    main()
