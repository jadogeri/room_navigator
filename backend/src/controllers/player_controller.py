"""
Player Controller Module
------------------------
Description: Controller for handling Player requests.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-APR-19
File: player_controller.py
License: MIT
"""
from flask import jsonify, request, abort
from src.services.player_service import PlayerService
from src.entities.actors.player import PlayerEntity


class PlayerController:
    def __init__(self):
        self.service = PlayerService()

    def create(self):
        data = request.json
        # Use the pure PlayerEntity class
        new_player = PlayerEntity(
            name=data['name'],
            health=data.get('health', 100),
            speed=data.get('speed', 10),
            damage=data.get('damage', 5)
        )
        saved = self.service.create_player(new_player)
        return jsonify({"id": saved.id, "message": "Player created"}), 201

    def list_all(self):
        players = self.service.get_all_players()
        return jsonify([{"id": p.id, "name": p.name} for p in players]), 200

    def get_one(self, id: str):
        player = self.service.get_player_by_id(id)
        if not player:
            abort(404)
        return jsonify({"id": player.id, "name": player.name, "health": player.health}), 200

    def update(self, id: str):
        if self.service.update_player(id, request.json):
            return jsonify({"message": "Player updated"}), 200
        abort(404)

    def delete(self, id: str):
        if self.service.delete_player(id):
            return jsonify({"message": "Player deleted"}), 200
        abort(404)
