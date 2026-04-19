"""
Square Module
-------------
Description: Represents a square in the game world, which can hold an occupant
             and link to adjacent squares.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2023-10-27
File: square.py
License: MIT
"""
from __future__ import annotations # MUST BE LINE 1
from src.constants import INVALID_SQUARE_ERROR, INVALID_OCCUPANT_ERROR
from src.interfaces.placeable import Placeable
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.interfaces.placeable import Placeable
from nanoid import generate


class Square:
    def __init__(
        self, 
        occupant: Optional[Placeable] = None,
        north: Optional[Square] = None, 
        south: Optional[Square] = None, 
        east: Optional[Square] = None, 
        west: Optional[Square] = None
    ):
        self.id: str = generate()
        self._occupant: Optional[Placeable] = None
        # Initialize internal storage to avoid AttributeError before setters run
        self._north: Square | None = None
        self._south: Square | None = None
        self._east: Square | None = None
        self._west: Square | None = None
        
        # Use setters for initial assignment to trigger linking logic
        self.north = north
        self.south = south
        self.east = east
        self.west = west    
        self.occupant = occupant


    @property
    def occupant(self) -> Placeable | None:
        return self._occupant

    @occupant.setter
    def occupant(self, value: Placeable | None):
        # The isinstance check works because of @runtime_checkable
        if value is not None and not isinstance(value, Placeable):
            raise ValueError(INVALID_OCCUPANT_ERROR);
        self._occupant = value


    # --- North Property ---
    @property
    def north(self) -> Optional[Square]:
        return self._north

    @north.setter
    def north(self, value: Optional[Square]):
        if value is not None and not isinstance(value, Square):
            raise ValueError(INVALID_SQUARE_ERROR)
        self._north = value
        # Auto-link: My north's south is me
        if value is not None and value.south is not self:
            value.south = self

    # --- South Property ---
    @property
    def south(self) -> Optional[Square]:
        return self._south

    @south.setter
    def south(self, value: Optional[Square]):
        if value is not None and not isinstance(value, Square):
            raise ValueError(INVALID_SQUARE_ERROR)
        self._south = value
        # Auto-link: My south's north is me
        if value is not None and value.north is not self:
            value.north = self

    # --- East Property ---
    @property
    def east(self) -> Optional[Square]:
        return self._east

    @east.setter
    def east(self, value: Optional[Square]):
        if value is not None and not isinstance(value, Square):
            raise ValueError(INVALID_SQUARE_ERROR)
        self._east = value
        # Auto-link: My east's west is me
        if value is not None and value.west is not self:
            value.west = self

    # --- West Property ---
    @property
    def west(self) -> Optional[Square]:
        return self._west

    @west.setter
    def west(self, value: Optional[Square]):
        if value is not None and not isinstance(value, Square):
            raise ValueError(INVALID_SQUARE_ERROR)
        self._west = value
        # Auto-link: My west's east is me
        if value is not None and value.east is not self:
            value.east = self

    def __eq__(self, other: object) -> bool:
        # A square is only equal to itself
        return self is other

    def __hash__(self) -> int:
        # The hash is based on the unique identity of this specific square
        return hash(id(self))

    def __repr__(self) -> str:
        # Simplified to show presence of neighbors without recursion
        n = "Square" if self.north else "None"
        s = "Square" if self.south else "None"
        e = "Square" if self.east else "None"
        w = "Square" if self.west else "None"
        return f"Square(N:{n}, S:{s}, E:{e}, W:{w})"
    
    def to_dict(self) -> dict:
        # Non-recursive dict representation
        return {
            "north": "Square" if self.north else None,
            "south": "Square" if self.south else None,
            "east": "Square" if self.east else None,
            "west": "Square" if self.west else None,
            "occupant": self.occupant.name if self.occupant else None
        }


