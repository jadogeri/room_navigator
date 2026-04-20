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
from __future__ import annotations
from extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

class PlayerModel(db.Model):
    __tablename__ = "players"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    health: Mapped[int] = mapped_column(Integer, default=100)
    speed: Mapped[int] = mapped_column(Integer, default=10)
    damage: Mapped[int] = mapped_column(Integer, default=5)

    def __repr__(self) -> str:
        return f"<PlayerModel {self.name}>"
