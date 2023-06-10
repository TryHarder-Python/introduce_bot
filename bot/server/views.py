from aiogram import Bot
from aiogram.utils.web_app import check_webapp_signature
from aiohttp import web
from aiohttp.web_response import json_response


async def check_data_handler(request: web.Request):
    bot: Bot = request.app["bot"]
    data = await request.post()
    if check_webapp_signature(bot.token, data["_auth"]):
        return json_response({"ok": True})
    return json_response({"ok": False, "err": "Unauthorized"}, status=401)
