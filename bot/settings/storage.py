import os

from aiogram.fsm.storage.redis import RedisStorage

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

STORAGE = RedisStorage.from_url(REDIS_URL + '/0')


