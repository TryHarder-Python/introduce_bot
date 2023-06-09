import os
from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent.parent.joinpath('.env')

load_dotenv(dotenv_path=ENV_PATH)


TOKEN = os.getenv('TOKEN')

REDIS_URL = os.getenv('REDIS_URL', 'redis://127.0.0.1:6378')

WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'https://d525-194-104-22-246.ngrok-free.app')

APP_HOST = os.getenv('APP_HOST', default='localhost')
APP_PORT = os.getenv('APP_PORT', default=5000)

