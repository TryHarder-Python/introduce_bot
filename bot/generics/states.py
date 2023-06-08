from aiogram.fsm.state import StatesGroup, State


class RepostState(StatesGroup):
    send_text = State()
    choice_url = State()
    preview_post = State()
    