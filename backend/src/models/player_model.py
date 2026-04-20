
"""
Player Model Module
-------------------
Description: SQLAlchemy database model for Player persistence.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: player_model.py
License: MIT
"""
from extensions import db

class PlayerModel(db.Model):
    __tablename__ = 'players'

    # ID is a string to support nanoid or UUIDs if needed
    id: str = db.Column(db.String(36), primary_key=True)
    name: str = db.Column(db.String(80), nullable=False)
    health: int = db.Column(db.Integer, default=100)
    speed: int = db.Column(db.Integer, default=10)
    damage: int = db.Column(db.Integer, default=5)

    def __repr__(self) -> str:
        return f'<PlayerModel {self.name}>'
