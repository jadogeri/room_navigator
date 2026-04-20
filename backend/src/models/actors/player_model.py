# src/models/player_model.py
from extensions import db

class PlayerModel(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    health = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    damage = db.Column(db.Integer)
