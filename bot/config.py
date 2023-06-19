import os
from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent.parent.joinpath('.env')

load_dotenv(dotenv_path=ENV_PATH)


TOKEN = os.getenv('TOKEN')

REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379')

WEBHOOK_URL = os.getenv('WEBHOOK_HOST')
WEBHOOK = WEBHOOK_URL is not None
APP_HOST = os.getenv('APP_HOST', default='localhost')
APP_PORT = os.getenv('APP_PORT', default=5000)

