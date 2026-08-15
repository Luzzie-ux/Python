#!/usr/bin/env python3
# mypy: disable-error-code="import-not-found"
# mypy: disable-error-code="misc"
# mypy: disable-error-code="untyped-decorator"

"""Directory: ex2/.

Files to Submit: space_crew.py
Authorized: None
"""

import random
import sys
from enum import Enum

try:
    from datetime import UTC, datetime

    from pydantic import (
        BaseModel,
        Field,
        ValidationError,
        model_validator,
    )
except (ModuleNotFoundError, ImportError) as e:
    print(f"{e.__class__.__name__}: {e}", file=sys.stderr)
    sys.exit(1)


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIETENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> SpaceMission:
        if not self.mission_id.startswith("M"):
            errmsg: str = "Mission ID must start with 'M' "
            raise ValueError(errmsg)
        leaders: tuple[Rank, Rank] = (Rank.COMMANDER, Rank.CAPTAIN)
        if not any(member.rank in leaders for member in self.crew):
            rankerr: str = (
                "Mission must have at least one Commander or Captain"
            )
            raise ValueError(rankerr)
        if self.duration_days > 365:
            experienced: int = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced < len(self.crew) / 2:
                experr: str = (
                    "Long missions (> 365 days) need 50% experienced crew"
                )
                raise ValueError(experr)
        if not all(member.is_active for member in self.crew):
            activerr: str = "All crew members must be active"
            raise ValueError(activerr)
        return self

    def display(self) -> None:
        print("=" * 39)
        print("Valid mission created:")
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days}")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew member:")
        for member in self.crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )
        print("=" * 39)


def make_crew(n: int) -> list[CrewMember]:
    names: list[str] = ["Sarah Connor", "John Smith", "Alice Johnson"]
    ranks: list[Rank] = [Rank.COMMANDER, Rank.LIETENANT, Rank.OFFICER]
    specs: list[str] = ["Mission Command", "Navigation", "Engineering"]
    crew: list[CrewMember] = []
    for i in range(n):
        mid: str = "CM0" + str(i)
        member = CrewMember(
            member_id=mid,
            name=names[i],
            rank=ranks[i],
            age=int(random.randint(18, 80)),
            specialization=specs[i],
            years_experience=int(random.randint(5, 50)),
        )
        crew.append(member)
    return crew


def main() -> None:
    test: int = 3
    print("Space Mission Crew Validation")
    crew: list[CrewMember] = make_crew(test)
    valid = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 12, 6, tzinfo=UTC),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )
    valid.display()
    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Survey",
            destination="Moon",
            launch_date=datetime(2024, 12, 1, tzinfo=UTC),
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob Wilson",
                    rank=Rank.CADET,
                    age=22,
                    specialization="Geology",
                    years_experience=1,
                ),
            ],
            budget_millions=150.0,
        )
    except ValidationError as error:
        print("Expected validation error:")
        msg: str = error.errors()[0]["msg"]
        print(msg.removeprefix("Value error, "))


if __name__ == "__main__":
    main()
