"""
Placeable Interface
-------------------
Description: Defines the interface for any object that can occupy a Square in the game world.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2023-10-27
File: placeable.py
License: MIT
"""

from abc import ABC
    
class Placeable(ABC):
    """
    The Placeable protocol defines the interface for any object that can 
    occupy a Square in the game world.
    
    This includes static objects (furniture, notes), items (weapons, keys), 
    and living entities (players, monsters).
    """

    name: str  
    """The display name of the object used in menus and room descriptions."""

    def get_examine_text(self) -> str:
        """
        Provides a detailed sensory description of the object.
        
        Returns:
            str: The flavor text shown when the player explicitly 
                 inspects the object.
        """
        pass
