#!/usr/bin/env python3

import alchemy


def main() -> None:
    print("=== Transmutation 2 ===")
    print(
        "Using import alchemy only\n"
        + f"Testing lead to gold: {alchemy.lead_to_gold()}"
    )
    return


if __name__ == "__main__":
    main()
