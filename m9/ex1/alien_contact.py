#!/usr/bin/env python3
# mypy: disable-error-code="import-not-found"
# mypy: disable-error-code="misc"
# mypy: disable-error-code="untyped-decorator"

"""
Directory: ex1/
Files to Submit: alien_contact.py
Authorized: None
"""

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
        if not self.acontact_id.startswith("AC"):
            iderr: str = "Contact ID must start with AC (Alien Contact)"
            raise ValueError(iderr)
        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                verr: str = "Physical contact reports must be verified"
                raise ValueError(verr)
        if self.contact_type == ContactType.TELEPATHIC:
            required_witness: int = 3
            if self.witness_count < required_witness:
                werr: str = (
                    "Telepathic contact requires at least "
                    f"{required_witness} witnesses"
                )
                raise ValueError(werr)
        strong: float = 7.0
        if self.signal_strength > strong:
            if not self.message_received:
                sigerr: str = (
                    f"Strong signals (> {strong}) "
                    "should include received messages"
                )
                raise ValueError(sigerr)
        return self

    def display(self) -> None:
        print("=" * 39)
        print("Valid contact report:")
        print(f"ID: {self.acontact_id}")
        print(f"Type: {self.contact_type.value}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes}")
        print(f"Witness: {self.witness_count}")
        if not self.message_received:
            print("Message: None")
        print(f"Message: '{self.message_received}'")
        print()
        print("=" * 39)


def main() -> None:
    print("Alien Contact Log")
    valid = AlienContact(
        acontact_id="AC_2024_011",
        timestamp=datetime(year=2024, month=1, day=1, tzinfo=UTC),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    valid.display()
    try:
        AlienContact(
            acontact_id="AC_2022_033",
            timestamp=datetime(year=2022, month=3, day=3, tzinfo=UTC),
            location="Moonshine Farm",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=10.0,
            duration_minutes=45,
            witness_count=1,
        )
    except ValidationError as e:
        print("Expected validation error:", file=sys.stderr)
        msg: str = e.errors()[0]["msg"]
        print(msg.removeprefix("Value error, "), file=sys.stderr)


if __name__ == "__main__":
    main()
