
"""
Player Routes Module
--------------------
Description: Flask blueprint for Player endpoints.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2026-APR-19
File: player_routes.py
License: MIT
"""
from flask import Blueprint
from src.controllers.player_controller import PlayerController

player_bp = Blueprint('player_routes', __name__)
pc = PlayerController()

@player_bp.route('', methods=['POST'])
def create_player(): return pc.create()

@player_bp.route('', methods=['GET'])
def get_players(): return pc.list_all()

@player_bp.route('/<string:id>', methods=['GET'])
def get_player(id): return pc.get_one(id)

@player_bp.route('/<string:id>', methods=['PUT'])
def update_player(id): return pc.update(id)

@player_bp.route('/<string:id>', methods=['DELETE'])
def delete_player(id): return pc.delete(id)
