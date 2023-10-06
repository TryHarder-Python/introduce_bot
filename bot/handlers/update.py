from typing import Any

from aiogram import Router, types, F
from aiogram.enums import ChatType

from aiogram.filters import Command, ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.types import Message, ChatMemberUpdated

update_router = Router()


@update_router.chat_member(
    ChatMemberUpdatedFilter(JOIN_TRANSITION),
    F.chat.type == ChatType.CHANNEL
)
async def welcome(event: ChatMemberUpdated) -> Any:
    return event.answer()


