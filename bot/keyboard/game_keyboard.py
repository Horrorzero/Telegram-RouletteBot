from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_game_inline_markup():
    builder = InlineKeyboardBuilder()

    for i in range(1,5):
        builder.add(InlineKeyboardButton(text=str(i),callback_data=str(i)))

    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)