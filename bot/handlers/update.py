from typing import Any

from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError

from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.types import ChatMemberUpdated

update_router = Router()


@update_router.chat_member(
    ChatMemberUpdatedFilter(JOIN_TRANSITION),
    F.chat.type == ChatType.CHANNEL
)
async def welcome(event: ChatMemberUpdated) -> Any:
    try:
        await event.bot.send_message(
            chat_id=event.from_user.id,
            text=(
                'Hey there 👋🏼 Brad here from the Weekly Investor! Thanks for subscribing to our channel.\n'
                'If you need more information on how our trading systems work, you can reach me at '
                '@WeeklyInvestorSupport 📥'
            ),
        )
    except (TelegramBadRequest, TelegramForbiddenError):
        pass


