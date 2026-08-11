#!/usr/bin/env python3

"""
Directory: ex0/
Files to Submit: space_station.py
Authorized: None
"""

import sys
from datetime import datetime

try:
    from pydantic import BaseModel, Field, ValidationError
except (ModuleNotFoundError, ImportError) as e:
    print(f"{e.__class__.__name__}: {e}", file=sys.stderr)
    sys.exit(1)


class SpaceStation(BaseModel):
    """Space Station Base Model"""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)

    def display(self) -> None:
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        print(f"Last Maintenance: {self.last_maintenance}")
        print("Status: ", end="")
        if not self.is_operational:
            print("Non", end=" ")
        print("Operational")
        if self.notes:
            print(f"Notes: {self.notes}")
        print()


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 20)

    valid = SpaceStation(
        station_id="ISS001",
        name=" International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2000, 2, 12),
        is_operational=True,
        notes="Everything alright",
    )
    print("Valid station created:")
    valid.display()
    print("=" * 20)
    try:
        invalid = SpaceStation(
            station_id="ISS002",
            name=" International Space Station",
            crew_size=21,
            power_level=30.2,
            oxygen_level=50.0,
            last_maintenance=datetime(2021, 6, 18),
            is_operational=True,
            notes="Everything not alright",
        )
        invalid.display()
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
