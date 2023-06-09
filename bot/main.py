import logging

from aiogram import Dispatcher, Bot

from aiogram.webhook.aiohttp_server import setup_application, SimpleRequestHandler
from aiohttp.web import run_app
from aiohttp.web_app import Application

import config
from misc import storage, BOT
from routers import RouterService
from server.server import init_app


# async def main() -> None:
#     dp = Dispatcher(storage=STORAGE)
#     dp.include_router(RouterService.collect_my_routers())
#     await BOT.set_my_commands(RouterService.collect_my_commands())
#     await dp.start_polling(BOT)


async def on_startup(bot: Bot, base_url: str):
    await bot.set_webhook(f"{base_url}/webhook")


def main():
    dp = Dispatcher(storage=storage)

    dp["base_url"] = config.WEBHOOK_URL
    dp.startup.register(on_startup)

    dp.include_router(RouterService.collect_my_routers())

    app = Application()
    app["BOT"] = BOT

    init_app(app)
    SimpleRequestHandler(
        dispatcher=dp,
        bot=BOT,
    ).register(app, path="/webhook")
    setup_application(app, dp, bot=BOT)
    run_app(app, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

