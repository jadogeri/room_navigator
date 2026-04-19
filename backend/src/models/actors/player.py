from typing import Optional
from nanoid import generate

from extensions import db
from src.interfaces.base_actor import Actor
from src.models.world.square import Square
from src.schemas.interaction import InteractionResult

class Player(db.Model):
    """
    Concrete Player class that implements the Actor interface,
    the GameObject interface, and functions as a SQLAlchemy model.
    """
    __tablename__ = 'players'
    
    # 1. Database Columns (also satisfies GameObject 'id' requirement)
    id = db.Column(db.String(10), primary_key=True, default=lambda: generate(size=10))
    name = db.Column(db.String(100), nullable=False)
    health = db.Column(db.Integer, nullable=False, default=100)
    speed = db.Column(db.Integer, nullable=False, default=10)
    damage = db.Column(db.Integer, nullable=False, default=5)

    def __init__(self, name: str, health: int, speed: int, damage: int):
        # 2. Call Parent Constructors Explicitly
        db.Model.__init__(self)
        Actor.__init__(self, name, health, speed, damage)

    # --- Implementation of GameObject Abstract Methods ---
    # (Assuming GameObject defines these; adjust based on your actual source)
    
    def get_id(self) -> str:
        """Requirement from GameObject interface."""
        return self.id

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

    def __repr__(self):
        return f"<Player {self.name} ID={self.id}>"
