import os
from flask import Flask
from extensions import db
from routes.player_routes import player_bp

# Define basedir here so it's relative to this file
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    
    # Absolute path for the DB file
    db_path = os.path.join(basedir, 'game.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from src.models.player_model import PlayerModel
        db.create_all()

    # Registered with your api/v1 prefix
    app.register_blueprint(player_bp, url_prefix='/api/v1/players')
    
    return app

