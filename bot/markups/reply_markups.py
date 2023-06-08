from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def revert_to_chanel_setup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text='Return to set channel for repost')
    return builder.as_markup(resize_keyboard=True)


def default_url_setup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="CLICK HERE TO MESSAGE - https://t.me/weeklyinvestorsupport"),
        KeyboardButton(text="T4 TRADE - https://go.t4trade.com/visit/?bta=36053&nci=5361"),
        KeyboardButton(text="MULTIBANK FX - https://go.mexnetpro.com/visit/?bta=35221&nci=5464"),
        KeyboardButton(text="Return to set channel for repost"),
    )
    builder.adjust(1)
    builder.as_markup(resize_keyboard=True)
    return builder.as_markup(resize_keyboard=True)


def default_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="Preview post"),
        KeyboardButton(text="Send post"),
        KeyboardButton(text="Return to set channel for repost"),
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

