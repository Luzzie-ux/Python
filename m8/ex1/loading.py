#!/usr/bin/env python3


"""
Directory: ex1/
Files to Submit: loading.py, requirements.txt, pyproject.toml
Authorized: pandas, requests, matplotlib, numpy, sys, importlib
"""

from importlib import import_module

pd= import_module("pandas")
np= import_module("numpy")
mpl = import_module("matplotlib")
plt = import_module("matplotlib.pyplot")
req = import_module("requests")

def main() -> None:
    print("This is the loading module!")

    print(pd.__name__)
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    for n in s:
        print(n)
    dates = pd.date_range("20130101", periods=6)
    print(dates)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print()
    print(df)
    print(df.dtypes)
    print()
    df2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
    )
    print(df2)
    print(df2.dtypes)
    print()
    print(np.__name__)
    return


if __name__ == "__main__":
    main()
