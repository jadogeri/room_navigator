from flask import Flask
from backend.src.extensions import db
from dotenv import load_dotenv
import os

def create_app():
    app: Flask = Flask(__name__)

    # 1. Config (Must be set BEFORE db.init_app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['RESTX_MASK_SWAGGER'] = False
    # Link to a popular dark theme for Swagger

    # 2. Initialize Extensions
    db.init_app(app)



    # 5. Register Blueprint with the URL prefix
    app.register_blueprint(app, url_prefix='/api/v1')

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