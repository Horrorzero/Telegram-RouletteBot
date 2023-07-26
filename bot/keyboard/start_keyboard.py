from aiogram.types import KeyboardButton,  ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_menu_reply_markup() -> ReplyKeyboardMarkup:
    buttons = [
        "Профіль", "Грати",
        "Правила"
    ]

    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.add(KeyboardButton(text=button))
    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)

