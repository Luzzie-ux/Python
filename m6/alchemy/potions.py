from elements import create_fire, create_water

from alchemy.elements import create_air, create_earth

__all__: list[str] = ["healing_potion", "strength_potion"]


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
    )
