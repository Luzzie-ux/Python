#!/sur/bin/env python3

from light_validator import validate_ingredients

__all__: list[str] = ["light_spell_allowed_ingredients", "light_spell_record"]

def light_spell_allowed_ingredients() -> list[str]: return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) -> str: ...