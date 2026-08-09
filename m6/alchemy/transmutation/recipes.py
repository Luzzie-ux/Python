#!/usr/bin/env python3

from elements import create_fire

from alchemy.potions import strength_potion as buff

from .. import create_air

__all__: list[str] = ["lead_to_gold"]


def lead_to_gold() -> str:
    recipe: str = (
        "Recipe transmuting Lead to Gold: brew "
        + f"'{create_air()}' and '{buff()}' mixed with '{create_fire()}'."
    )
    return recipe
