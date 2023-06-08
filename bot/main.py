import asyncio
import logging

from aiogram import Dispatcher

from routers import RouterService
from settings import BOT


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(RouterService.collect_my_routers())
    await BOT.set_my_commands(RouterService.collect_my_commands())
    await dp.start_polling(BOT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
