from aiogram.filters.callback_data import CallbackData


class RepostCallbackFactory(CallbackData, prefix='fabnearby'):
    action: str
