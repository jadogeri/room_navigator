from nanoid import generate

from backend.src.interfaces.base_actor import Actor
from src.interfaces.placeable import Placeable
from src.constants import INVALID_HEALING_AMOUNT_ERROR

class Potion(Actor, Placeable):
    """A consumable item that heals the player."""
    
    def __init__(self, name: str, healing_amount: int):
        self.name = name
        self.healing_amount = healing_amount

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def healing_amount(self) -> int:
        return self._healing_amount

    @healing_amount.setter
    def healing_amount(self, value: int):
        if value < 0:
            raise ValueError(INVALID_HEALING_AMOUNT_ERROR)
        self._healing_amount = value

    def interact(self) -> str:
        # Implementation of the 'Placeable' contract
        return f"You drink the {self.name}. Your wounds begin to knit shut, restoring {self.healing_amount} health."

    def get_examine_text(self) -> str:
        # Implementation of the 'Placeable' contract
        return f"A small glass vial filled with a bubbling, crimson liquid. It restores {self.healing_amount} health."