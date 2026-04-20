# src/models/player_model.py
from extensions import db

class PlayerModel(db.Model):
    """
    Concrete Player class that implements the Actor interface,
    the GameObject interface, and functions as a SQLAlchemy model.
    """
    __tablename__ = 'players'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    health = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    damage = db.Column(db.Integer)
