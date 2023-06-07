from aiogram import Router
from aiogram.types import BotCommand


class RouterService:
    router = Router()
    commands = {
        'start': 'Start the bot',
        'support': 'Support',
        't4trade': 'T4 Trade',
        'multibankfx': 'MultiBank FX',
    }

    @classmethod
    def collect_my_commands(cls) -> list:
        """
        This function collect all commands from all routers
        """
        return [
            BotCommand(command=command, description=description)
            for command, description in cls.commands.items()
        ]
