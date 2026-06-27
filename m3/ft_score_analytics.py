#!/usr/bin/env python3

"""
Directory: ex1/
Files to Submit: ft_score_analytics.py
Authorized: import sys, sys.argv, len(), sum(), max(), min(), print()
"""

import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    index: int = len(sys.argv)
    arg: int = 0
    try:
        if index != 1:
            for i in range(1, index):
                try:
                    arg += int(sys.argv[i])
                except ValueError:
                    print(f"Invalid parameter '{sys.argv[i]}'")
                    print("No scores provided.", end=" ")
                    print(f"Usage: python3 {sys.argv[0]} <score1> <score2>")
                    return
            print("Scores processed: [", end="")
            for i in range(1, index - 1):
                print(f"{sys.argv[i]},", end=" ")
            print(f"{sys.argv[index - 1]}]")
            print(f"Total players: {index - 1}")
            print(f"Total score: {arg}")
            print(f"Average score: {arg / (index - 1)}")
            print(f"High score: {max(sys.argv[1:])}")
            print(f"Low Score: {min(sys.argv[1:])}")
            print(f"Score range: {int(max(sys.argv[1:])) -
                                  int(min(sys.argv[1:]))}")
        else:
            print("No scores provided.", end=" ")
            print(f"Usage: python3 {sys.argv[0]} <score1> <score2>")
    except ValueError:
        print(f"Invalid parameter '{arg}'")
        print("No scores provided.", end=" ")
        print(f"Usage: python3 {sys.argv[0]} <score1> <score2>")
    return


if __name__ == "__main__":
    ft_score_analytics()
