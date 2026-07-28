#!/usr/bin/env python3

import alchemy.transmutation as transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print(
        "Import transmutation module directly\n"
        + f"Testing lead to gold: {transmutation.lead_to_gold()}"
    )
    return


if __name__ == "__main__":
    main()
