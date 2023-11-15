from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()


@start_router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        'Welcome! Subscribe to this channel:\n'
        '⬇️⬇️⬇️⬇️\n'
        'https://t.me/weeklyinvestor',
    )
