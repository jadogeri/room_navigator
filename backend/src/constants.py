"""
Haunted House Game Constants
----------------------------
Description: Defines global constants and configuration values for the Haunted House Game, 
             including game settings, item definitions, and monster attributes.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-04-19
File: constants.py
License: MIT
"""

from typing import Final                
# Error Messages
INVALID_SQUARE_ERROR: Final[str] = "Value must be a Square or None"
INVALID_ACTOR_ERROR: Final[str] = "Value must be an Actor or None"
INVALID_OCCUPANT_ERROR: Final[str] = "Occupant must follow the Placeable protocol"
INVALID_HEALING_AMOUNT_ERROR: Final[str] = "Healing amount cannot be negative."

# Game Balance Defaults
DEFAULT_PLAYER_HP: Final[int] = 100
DEFAULT_INVENTORY_SIZE: Final[int] = 10