from aiogram import Router, F, Bot

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from generics.filters import EntitiesFilter
from generics.states import RepostState
from markups import inline_markups, reply_markups

repost_router = Router()

repost_router.message.filter(F.from_user.id.in_({660052222, 1273208116}))


@repost_router.message(Command(commands=["repost"]))
@repost_router.message(F.text.startswith('Return'))
async def repost_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(None)
    await message.answer(
        'Forward me a message from channel, where i am have permission to post',
    )


@repost_router.message(F.forward_from_chat)
async def channel_url_handler(message: Message, bot: Bot, state: FSMContext) -> None:
    chat_id = message.forward_from_chat.id
    data = await bot.get_chat_administrators(chat_id=chat_id)
    if not any(i for i in data if i.user.id == bot.id and i.can_post_messages):
        await message.answer('I am not in this channel or have not permission to post messages')
        return
    await state.set_data({'chat_id': chat_id}, )
    await change_text_handler(message, state)


@repost_router.message(F.text == 'Change text')
async def change_text_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(RepostState.send_text)
    await message.answer('Send post text', reply_markup=reply_markups.revert_to_chanel_setup())


@repost_router.message(RepostState.send_text)
async def send_text_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(message_id=message.message_id)
    await state.set_state(RepostState.choice_url)
    await message.answer(
        'Send url for post buttons in format: \n'
        'Button 1 - https://google.com\n'
        'Button 2 - http://example.com\n',
        reply_markup=reply_markups.default_url_setup(),
    )


@repost_router.message(RepostState.choice_url, F.text.regexp(r'^.* - .*'), EntitiesFilter('url'))
async def choice_url_handler(message: Message, state: FSMContext) -> None:
    text = message.text
    buttons = {}
    for button in text.split('\n'):
        button_text, url = button.split(' - ')
        buttons[button_text] = url
    await state.update_data(buttons={**buttons})
    await state.set_state(RepostState.preview_post)
    await message.answer('Now you can a post to your channel', reply_markup=reply_markups.default_menu())


@repost_router.message(RepostState.choice_url)
async def invalid_text(message: Message) -> None:
    await message.answer(
        'Invalid text, send url for post buttons in format: \n'
        'Button 1 - https://google.com\n'
        'Button 2 - http://example.com\n',
        reply_markup=reply_markups.default_url_setup(),
    )



@repost_router.message(F.text == 'Preview post', RepostState.preview_post)
async def preview_post_handler(message: Message, state: FSMContext, bot: Bot) -> None:
    data = await state.get_data()
    await bot.copy_message(
        chat_id=message.chat.id,
        from_chat_id=message.chat.id,
        message_id=data['message_id'],
        reply_markup=inline_markups.url_buttons(data['buttons'])
    )


@repost_router.message(F.text == 'Send post')
async def send_post_handler(message: Message, bot: Bot, state: FSMContext) -> None:
    data = await state.get_data()
    await bot.copy_message(
        chat_id=data['chat_id'],
        from_chat_id=message.chat.id,
        message_id=data['message_id'],
        reply_markup=inline_markups.url_buttons(data['buttons'])
    )
    await message.answer('Post sent')


@repost_router.message(Command(commands=["clear"]))
async def clear_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer('State cleared')
