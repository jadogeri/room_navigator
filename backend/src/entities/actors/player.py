
"""
Player Entity Module
---------------------
Description: Represents the Player entity in the game.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: player.py
License: MIT
"""

from src.interfaces.base_actor import Actor


class Player(Actor):
    def __init__(self, name, health=100, speed=10, damage=5, id=None):
        super().__init__(name, health, speed, damage)
        self.name = name
        self.health = health
        self.speed = speed
        self.damage = damage

    def get_info(self):
        return f"Player {self.name}: HP={self.health}, Speed={self.speed}, Damage={self.damage}"

    def attack(self, target):
        target.health -= self.damage


    def __repr__(self):
        return f"<Player {self.name} ID={self.id}>"
















    def render(self) -> str:
        """Visual representation requirement for GameObject."""
        return f"P[{self.name[0].upper()}]"

    # --- Implementation of Actor Abstract Methods ---

    def get_action_message(self) -> str:
        """Narrative text for the actor's current state."""
        return f"{self.name} is ready for action with {self.health} HP."

    def interact_with(self, target: 'Actor') -> InteractionResult:
        """
        Defines behavior when meeting another actor.
        Returns an InteractionResult (assumed schema).
        """
        # Example logic: Basic attack
        target.health -= self.damage
        return InteractionResult(
            message=f"{self.name} strikes {target.name} for {self.damage} damage!",
            success=True
        )

    def move(self, target_square: Square) -> Optional[Square]: 
        """
        Moves the player to a new square if it is not occupied.
        """
        if self.can_move_to(target_square):
            # Update internal location tracking
            self.current_square = target_square
            return target_square
        return None
