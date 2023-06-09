from aiogram import Router
from aiogram.types import BotCommand

from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from aiogram import Bot

from aiogram.utils.web_app import check_webapp_signature


class RouterService:
    router = Router()
    commands = {
        'start': 'Start the BOT'
    }

    @classmethod
    def collect_my_routers(cls) -> Router:
        """
        This function collect all routers from all routers
        """
        from handlers import start, repost
        cls.router.include_router(start.start_router)
        cls.router.include_router(repost.repost_router)
        return cls.router

    @classmethod
    def collect_my_commands(cls) -> list:
        """
        This function collect all commands from all routers
        """
        return [
            BotCommand(command=command, description=description)
            for command, description in cls.commands.items()
        ]

