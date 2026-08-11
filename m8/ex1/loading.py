#!/usr/bin/env python3


"""
Directory: ex1/
Files to Submit: loading.py, requirements.txt, pyproject.toml
Authorized: pandas, requests, matplotlib, numpy, sys, importlib
"""

import sys
from importlib import import_module as imp
from importlib.metadata import version


def check() -> None:
    print("Checking dependencies:\n")
    modules: list[str] = ["numpy", "pandas", "matplotlib"]
    size: int = len(modules)
    pkgs = {}
    for name in modules:
        try:
            pkgs[name] = imp(name)
        except ImportError:
            print(f"[ERROR]: missing dependency - '{name}'")
            continue
    if not pkgs or len(pkgs.values()) < size:
        conflict(len(pkgs.values()) - size)
    for name in pkgs:
        print(f"[OK] {name}: ", end="")
        print(f"({version(name)})", end="")
        print(f" - {desc(name)} ready")
    return simulate()


def desc(name: str) -> str:
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


def conflict(n: int) -> None:
    print(f"\n[ERROR]: Required packages are missing. ({n})\n")
    print("To install with pip:")
    print("    pip install -r requirements.txt")
    print("    python loading.py")
    print("\nTo install with Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py")
    sys.exit(1)


def simulate() -> None:
    print("\nAnalyzing Matrix Data")
    import numpy as np  # type: ignore

    s: int = 10
    t: int = 10

    rng = np.random.default_rng(42)
    pairs = rng.integers(1, 10, size=(s, 2))

    matrix = np.zeros((s, t), dtype=np.int64)
    matrix[:, 0] = pairs[:, 0]
    matrix[:, 1] = pairs[:, 1]

    for col in range(2, t):
        matrix[:, col] = matrix[:, col - 1] + matrix[:, col - 2]

    print(f"Processing {s * t} data points")
    import pandas as pd  # type: ignore

    df = pd.DataFrame(
        matrix,
        index=[f"S{i}" for i in range(s)],
        columns=[f"T{i}" for i in range(t)],
    )

    print("Generating visualization\n")
    from matplotlib import pyplot as plt  # type: ignore

    fig, ax = plt.subplots()
    for seq_label in df.index:
        ax.plot(df.columns, df.loc[seq_label], label=seq_label)

    ax.set_yscale("log")
    ax.set_title("Matrix Data")
    ax.set_xlabel("Term index")
    ax.set_ylabel("Value")
    ax.legend()

    print(df)
    print()
    print(df.iloc[:, -1].describe())
    print()

    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
    plt.close(fig)


def manager() -> None:
    print()
    print("Dependency manager comparison:")
    print("  PIP:    reads requirements.txt and installs into the active env")
    print("          no automatic lock file — versions may drift over time")
    print("  Poetry: reads pyproject.toml, resolves and pins all versions in")
    print("          poetry.lock, and manages its own venv automatically")
    print()


def main() -> None:
    print(
        "\nLOADING STATUS: Loading programs... \n\n"
        f"Python Version: {sys.executable}\n"
        f"Current PATH: {sys.prefix}\n",
    )
    check()
    manager()


if __name__ == "__main__":
    main()
