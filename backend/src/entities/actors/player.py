"""
Player Entity Module
---------------------
Description: Represents the Player entity in the game, inheriting core 
             behavior from the Actor base class.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: player.py
License: MIT
"""
from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from src.interfaces.base_actor import Actor

# Prevent circular imports for type hinting
if TYPE_CHECKING:
    from src.entities.world.square import Square
    # Assuming InteractionResult is defined in a results or interfaces module
    from src.schemas.interaction import InteractionResult 


class Player(Actor):
    def __init__(
        self, 
        name: str, 
        health: int = 100, 
        speed: int = 10, 
        damage: int = 5, 
        id: Optional[str] = None
    ) -> None:
        """    
        Initializes a new Player instance.
        
        Args:
            name (str): The display name of the player.
            health (int): Starting health points.
            speed (int): Movement speed or initiative value.
            damage (int): Base damage dealt in combat.
            id (str | None): Unique identifier, typically provided by persistence layer.
        """
        super().__init__(name, health, speed, damage, id)

    def get_info(self) -> str:
        """Returns a string summary of the player's current status."""
        return f"Player {self.name}: HP={self.health}, Speed={self.speed}, Damage={self.damage}"

    def attack(self, target: Actor) -> None:
        """Reduces the health of the target actor based on player damage."""
        target.health -= self.damage

    def __repr__(self) -> str:
        """Standard Python representation of the Player object."""
        return f"<Player {self.name} ID={self.id} HP={self.health} Speed={self.speed} Damage={self.damage}>"
    
    def to_dict(self) -> dict:
        """Serializes the player attributes for JSON responses or persistence."""
        return {
            "id": self.id,
            "name": self.name,
            "health": self.health,
            "speed": self.speed,
            "damage": self.damage
        }

    def render(self) -> str:
        """Visual representation requirement for GameObject."""
        return f"P[{self.name[0].upper()}]"

    # --- Implementation of Actor Abstract Methods ---

    def get_action_message(self) -> str:
        """Narrative text for the actor's current state."""
        return f"{self.name} is ready for action with {self.health} HP."

    def interact_with(self, target: Actor) -> InteractionResult:
        """
        Defines behavior when meeting another actor.
        """
        from src.schemas.interaction import InteractionResult
        target.health -= self.damage
        return InteractionResult(
            message=f"{self.name} strikes {target.name} for {self.damage} damage!",
            success=True
        )

    def move(self, target_square: Square) -> Optional[Square]: 
        """
        Moves the player to a new square if valid.
        """
        if hasattr(self, 'can_move_to') and self.can_move_to(target_square):
            # Update internal location tracking
            # Note: Actor/Placeable logic should handle updating Square.occupant
            return target_square
        return None
