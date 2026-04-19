from flask import Flask
from extensions import db
from routes.player_routes import player_bp
from dotenv import load_dotenv
import os

load_dotenv();

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Imports here to avoid circular dependencies
        from models.actors.player import Player
        db.create_all()

    app.register_blueprint(player_bp)
    return app

if __name__ == '__main__':
    # 1. Load the .env file FIRST
    load_dotenv()

    app = create_app()

    # 2. Get the port from environment, default to 5000 if not found
    # Note: os.getenv returns a string, so you must cast it to an int
    port = int(os.getenv('PORT', 5000))

    # 3. Pass the port to the run method
    app.run(debug=True, port=port)



