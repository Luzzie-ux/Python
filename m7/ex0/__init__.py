# ex0/__init_.py



from .factory import CreatureFactory
from .factory_type import AquaFactory, FlameFactory

__all__: list[str] = [
    "AquaFactory",
    "CreatureFactory",
    "FlameFactory",
]
