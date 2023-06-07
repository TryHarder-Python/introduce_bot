import os

from aiogram import Bot

TOKEN = os.getenv('TOKEN')
env = os.environ

BOT = Bot(TOKEN, parse_mode='HTML')
