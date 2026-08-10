from .dark_validator import validate_ingredients

__all__: list[str] = ["dark_spell_allowed_ingredients", "dark_spell_record"]


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    valid: str = validate_ingredients(ingredients)
    if "VALID" in valid:
        return f"Spell Recorded: {spell_name} {valid}"
    return f"Spell rejected: {spell_name} {valid}"
