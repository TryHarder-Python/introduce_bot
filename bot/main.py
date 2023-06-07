import asyncio
import logging

from aiogram import Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboard import support_keyboard, t4_trade_keyboard, multibank_fx_keyboard
from routers import RouterService
from settings import BOT

# Bot token can be obtained via https://t.me/BotFather
# All handlers should be attached to the Router (or Dispatcher)
router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        'Welcome! Subscribe to this channel:\n'
        '⬇️⬇️⬇️⬇️\n'
        'https://t.me/+EyCaGA8aOhBiZTlk',
    )


@router.message(Command(commands=["support"]))
async def command_support_handler(message: Message) -> None:
    await message.answer(
        'Our support team is always ready to help you!',
        reply_markup=support_keyboard(),
    )


@router.message(Command(commands=["t4trade"]))
async def command_t4trade_handler(message: Message) -> None:
    await message.answer(
        'T4 Trade is a leading forex broker offering the most advanced trading tools,'
        ' 24-hour live support, zero commissions and tight spreads.',
        reply_markup=t4_trade_keyboard(),
    )


@router.message(Command(commands=["multibankfx"]))
async def command_multibankfx_handler(message: Message) -> None:
    await message.answer(
        'MultiBank FX is a leading forex and CFD broker offering the most advanced trading tools,'
        ' 24-hour live support, zero commissions and tight spreads.',
        reply_markup=multibank_fx_keyboard(),
    )


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)
    # And the run events dispatching
    await BOT.set_my_commands(RouterService.collect_my_commands())
    await dp.start_polling(BOT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
