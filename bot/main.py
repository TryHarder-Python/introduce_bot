import asyncio
import logging

from aiohttp.web import run_app
from aiohttp.web_app import Application

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

import config
from misc import storage, BOT
from routers import RouterService
from server.server import init_app

TELEGRAM_TOKEN = config.TOKEN
APP_BASE_URL = config.WEBHOOK_URL


async def on_startup(bot: Bot, base_url: str):
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(f"{base_url}/webhook")


async def pulling_main():
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(RouterService.collect_my_routers())

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = BOT
    # And the run events dispatching
    await bot.delete_webhook()
    await dp.start_polling(bot)


def main():
    bot = BOT
    dispatcher = Dispatcher(storage=storage)
    dispatcher["base_url"] = config.WEBHOOK_URL
    dispatcher.startup.register(on_startup)

    dispatcher.include_router(RouterService.collect_my_routers())

    app = Application()
    app["bot"] = bot

    init_app(app)
    SimpleRequestHandler(
        dispatcher=dispatcher,
        bot=bot,
    ).register(app, path="/webhook")
    setup_application(app, dispatcher, bot=bot)

    run_app(app, host=config.APP_HOST, port=config.APP_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if config.WEBHOOK:
        main()
    else:
        asyncio.run(pulling_main())
