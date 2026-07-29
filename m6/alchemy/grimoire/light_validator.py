#!/usr/bin/env python3


__all__: list[str] = ["validate_ingredients"]


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = light_spell_allowed_ingredients()
    check: bool = any(
        ingredient in ingredients.lower() for ingredient in allowed
    )
    status: str = "VALID" if check is True else "INVALID"
    return f"{ingredients} - {status}"
