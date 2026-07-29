#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    check: bool = any(
        ingredient in ingredients.lower() for ingredient in allowed
    )
    status: str = "VALID" if check is True else "INVALID"
    return f"{ingredients} - {status}"
