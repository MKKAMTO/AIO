import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = os.getenv('API_ID')
    API_HASH = os.getenv('API_HASH')
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    # Database configuration
    DB_URL = os.getenv('DB_URL')
    
    # Music service API keys
    DEEZER_ARL = os.getenv('DEEZER_ARL')
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    TIDAL_TOKEN = os.getenv('TIDAL_TOKEN')
    QOBUZ_EMAIL = os.getenv('QOBUZ_EMAIL')
    QOBUZ_PASSWORD = os.getenv('QOBUZ_PASSWORD')
    KKBOX_KEY = os.getenv('KKBOX_KEY')
    
    # Download settings
    DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH', './downloads')
