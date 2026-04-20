import os
from app import create_app
from dotenv import load_dotenv

def main():
    # 1. Load environment variables
    # This assumes .env is in the same folder as main.py
    load_dotenv(override=True)

    # 2. Initialize the app
    app = create_app()

    # 3. Get configuration from .env
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    print(f"--- Haunted House API Starting ---")
    print(f"Port: {port}")
    print(f"Database: game.db")
    
    # 4. Run the app
    app.run(debug=debug_mode, port=port)

if __name__ == '__main__':
    main()



