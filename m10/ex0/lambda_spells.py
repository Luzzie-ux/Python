#!/usr/bin/env python3


"""
Directory: ex0/
Files to Submit: lambda_spells.py
Authorized: map, filter, sorted, min, max, round, sum, len
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda p: p["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max(mages, key=lambda m: m["power"])["power"]
    min(mages, key=lambda m: m["power"])["power"]
    sum(mages, key=lambda m: m["power"]) / len(mages)
    return {}


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 114, "type": "weapon"},
        {"name": "Lightning Rod", "power": 112, "type": "relic"},
        {"name": "Ice Wand", "power": 62, "type": "armor"},
        {"name": "Earth Shield", "power": 100, "type": "accessory"},
    ]
    mages = [
        {"name": "Alex", "power": 70, "element": "shadow"},
        {"name": "Phoenix", "power": 77, "element": "lightning"},
        {"name": "Nova", "power": 52, "element": "earth"},
        {"name": "Jordan", "power": 76, "element": "light"},
        {"name": "Rowan", "power": 54, "element": "wind"},
    ]
    spells = ["flash", "earthquake", "fireball", "tornado"]
    print("\nTesting artifact sorter...")
    print(artifact_sorter(artifacts))

    print("\nTesting Power Filter...")
    print(power_filter(mages, 60))

    print("\nTesting spell transformer...")
    print(spell_transformer(spells))

    print("\nTesting Mage Stats")
    print(mage_stats(mages))

    return


if __name__ == "__main__":
    main()
