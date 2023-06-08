from aiogram.utils.keyboard import InlineKeyboardBuilder

from generics.callback_factories import RepostCallbackFactory


# def setup_keyboard():
#     menu_builder = InlineKeyboardBuilder()
#     menu_builder.button(
#         text='Радиус в метрах',
#         callback_data=RepostCallbackFactory(action=''),
#     )
#     menu_builder.button(
#         text='Тип места', callback_data=NearbySettingsCallbackFactory(action='type'),
#     )
#     menu_builder.button(
#         text='Ключевое слово',
#         callback_data=NearbySettingsCallbackFactory(action='keyword'),
#     )
#     menu_builder.adjust(2)
#     return menu_builder.as_markup()


def url_buttons(buttons: dict):
    menu_builder = InlineKeyboardBuilder()
    for text, url in buttons.items():
        menu_builder.button(
            text=text,
            url=url,
        )
    return menu_builder.as_markup()
