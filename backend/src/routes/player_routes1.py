from flask import Blueprint, request, jsonify
from extensions import db
from models.actors.player import Player

player_bp = Blueprint('player_routes', __name__)

@player_bp.route('/players', methods=['POST'])
def create_player():
    data = request.json
    new_player = Player(
        name=data['name'], 
        health=data.get('health', 100),
        speed=data.get('speed', 10),
        damage=data.get('damage', 5)
    )
    db.session.add(new_player)
    db.session.commit()
    return jsonify({"id": new_player.id, "message": "Player created"}), 201

@player_bp.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([{"id": p.id, "name": p.name} for p in players])

@player_bp.route('/players/<string:id>', methods=['GET'])
def get_player(id):
    player = Player.query.get_or_404(id)
    return jsonify({"id": player.id, "name": player.name, "health": player.health})

@player_bp.route('/players/<string:id>', methods=['PUT'])
def update_player(id):
    player = Player.query.get_or_404(id)
    data = request.json
    player.name = data.get('name', player.name)
    player.health = data.get('health', player.health)
    db.session.commit()
    return jsonify({"message": "Player updated"})

@player_bp.route('/players/<string:id>', methods=['DELETE'])
def delete_player(id):
    player = Player.query.get_or_404(id)
    db.session.delete(player)
    db.session.commit()
    return jsonify({"message": "Player deleted"})


