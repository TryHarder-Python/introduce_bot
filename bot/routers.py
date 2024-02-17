from aiogram import Router
from aiogram.types import BotCommand


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
        from handlers import start, repost, update
        cls.router.include_router(start.start_router)
        cls.router.include_router(repost.repost_router)
        cls.router.include_router(update.update_router)
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

