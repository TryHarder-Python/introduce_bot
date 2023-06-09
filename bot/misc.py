from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

import config

ROOT_DIR: Path = Path(__file__).parent.parent

storage = RedisStorage.from_url(config.REDIS_URL)

BOT = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=BOT, storage=storage)
