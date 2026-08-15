#!/usr/bin/env python3


"""Directory: ex0/.

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
    max_power: int = max(mages, key=lambda m: m["power"])["power"]
    min_power: int = min(mages, key=lambda m: m["power"])["power"]
    avg_power: float = sum(map(lambda m: m["power"], mages)) / len(mages)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


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
    a = artifact_sorter(artifacts)
    print(a)

    print("\nTesting Mage Stats")
    m = mage_stats(mages)
    print(m)

    print("\nTesting spell transformer...")
    s = spell_transformer(spells)
    print(s)

    print("\nTesting Power Filter...")
    p = power_filter(mages, m["avg_power"])
    print(p)


if __name__ == "__main__":
    main()
