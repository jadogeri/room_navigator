"""
Actor Interface
-------------------
Description: Defines the interface for any actor in the game world.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2023-10-27
File: base_actor.py
License: MIT
"""

from abc import ABC, abstractmethod
from typing import Optional

from src.interfaces.game_object import GameObject
from src.entities.world.square import Square
from src.schemas.interaction import InteractionResult

class Actor(GameObject, ABC):
    def __init__(self, name: str, health: int, speed: int, damage: int):
        super().__init__()
        self.name = name
        self.health = health
        self.speed = speed
        self.damage = damage
        self.current_square: Optional['Square'] = None

    @abstractmethod
    def get_action_message(self) -> str:
        """Narrative text for the actor's current state/action."""
        ...

    @abstractmethod
    def interact_with(self, target: 'Actor') -> InteractionResult:
        """
        Defines how this actor behaves when it meets another actor.
        Example: A Vampire attacks. A narrative description of the result of the interaction 
            to be displayed to the player
        """
        ...

    @abstractmethod
    def move(self, current_square: Square) -> Square | None:         
        pass

    # Concrete method to check if square is occupied
    def can_move_to(self, square: Square) -> bool:
        return square.occupant is None
    
    
