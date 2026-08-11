#!/usr/bin/env python3


"""
Directory: ex1/
Files to Submit: alien_contact.py
Authorized: None
"""
import sys
from datetime import UTC, datetime
from enum import Enum

try:
    from pydantic import (
        BaseModel,
        Field,
        ValidationError,
        model_validator,
    )
except (ModuleNotFoundError, ImportError) as e:
    print(f"{e.__class__.__name__}: {e}", file=sys.stderr)
    sys.exit(1)


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telephatic"


class AlienContact(BaseModel):
    acontact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validation(self) -> AlienContact:
        errmsg: str = "Something Went Wrong"
        if self.acontact_id.startswith("AC"):
            raise ValueError(errmsg)
        return self


def main() -> None:
    try:
        AlienContact(
        acontact_id="AC_2024_001",
        timestamp=datetime(year=2021, month=6, day=18, tzinfo=UTC),
        location="Earth",
        contact_type=ContactType.RADIO,
        signal_strength=5.0,
        duration_minutes=1440,
        witness_count=10,
        )
    except ValidationError as e:
        print(e)
    return


if __name__ == "__main__":
    main()
