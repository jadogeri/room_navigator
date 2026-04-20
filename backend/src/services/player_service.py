
"""
Player Service Module
---------------------
Description: Bridges pure PlayerEntity logic with the PlayerRepository.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: player_service.py
License: MIT
"""
from __future__ import annotations
from backend.src.repositories.base_repository import BaseRepository
from src.repositories.player_repository import PlayerRepository
from src.models.player_model import PlayerModel
from src.entities.actors.player import Player
from nanoid import generate

class PlayerService:
    def __init__(self):
        
        self.repository: BaseRepository = PlayerRepository()

    def create_player(self, entity: Player) -> Player:
        # 1. Assign ID if missing
        if not entity.id:
            entity.id = generate()
        
        # 2. Map Entity -> Model for database
        model = PlayerModel(
            id=entity.id,
            name=entity.name,
            health=entity.health,
            speed=entity.speed,
            damage=entity.damage
        )
        saved_entity = self.repository.save(model)
        return saved_entity
    
    def get_all_players(self) -> list[Player]:
        models = self.repository.get_all()
        return [
            Player(
                id=m.id,
                name=m.name,
                health=m.health,
                speed=m.speed,
                damage=m.damage
            ) for m in models
        ]

    def get_player_by_id(self, player_id: str) -> Player | None:
        model = self.repository.get_one(player_id)
        if not model:
            return None
            
        # 3. Map Model -> Entity for business logic
        return Player(
            id=model.id,
            name=model.name,
            health=model.health,
            speed=model.speed,
            damage=model.damage
        )

    def update_player(self, player_id: str, data: dict) -> bool:
        model = self.repository.get_one(player_id)
        if model:
            model.name = data.get('name', model.name)
            model.health = data.get('health', model.health)
            self.repository.save(model)
            return True
        return False

    def delete_player(self, player_id: str) -> bool:
        return self.repository.delete(player_id)
