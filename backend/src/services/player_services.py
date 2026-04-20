"""
Player Service Module
---------------------
Description: Business logic handling pure PlayerEntity objects.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-APR-19
File: player_service.py
License: MIT
"""
from __future__ import annotations
from src.repositories.player_repository import PlayerRepository
from src.entities.actors.player import PlayerEntity

class PlayerService:
    def __init__(self):
        self.repository = PlayerRepository()

    def create_player(self, entity: PlayerEntity) -> PlayerEntity:
        # Save to DB via repository
        saved_model = self.repository.save(entity)
        entity.id = saved_model.id
        return entity

    def get_all_players(self) -> list[PlayerEntity]:
        return self.repository.get_all()

    def get_player_by_id(self, player_id: str) -> PlayerEntity | None:
        return self.repository.get_one(player_id)

    def update_player(self, player_id: str, data: dict) -> bool:
        player = self.repository.get_one(player_id)
        if player:
            player.name = data.get('name', player.name)
            player.health = data.get('health', player.health)
            self.repository.save(player)
            return True
        return False

    def delete_player(self, player_id: str) -> bool:
        return self.repository.delete(player_id)
