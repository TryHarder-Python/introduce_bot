from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def support_keyboard():
    menu_builder = InlineKeyboardBuilder()
    menu_builder.add(
        InlineKeyboardButton(text="CLICK HERE TO MESSAGE", url="https://t.me/weeklyinvestorsupport"),
    )
    return menu_builder.as_markup()


def t4_trade_keyboard():
    menu_builder = InlineKeyboardBuilder()
    menu_builder.add(
        InlineKeyboardButton(text="T4 TRADE", url="https://go.t4trade.com/visit/?bta=36053&nci=5361"),
    )
    return menu_builder.as_markup()


def multibank_fx_keyboard():
    menu_builder = InlineKeyboardBuilder()
    menu_builder.add(
        InlineKeyboardButton(text="MULTIBANK FX", url="https://go.mexnetpro.com/visit/?bta=35221&nci=5464"),
    )
    return menu_builder.as_markup()