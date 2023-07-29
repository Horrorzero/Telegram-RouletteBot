from aiogram.types import InlineKeyboardButton,  InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_color_inline_markup():
    builder = InlineKeyboardBuilder()
    
    buttons = [
        InlineKeyboardButton(
            text="Чорний",
            callback_data="col_black"
        ),
        InlineKeyboardButton(
            text="Червоний",
            callback_data="col_red"
        ),
    ]

    for button in buttons:
        builder.add(button)
        
    builder.adjust(1)
    

    return builder.as_markup(resize_keyboard=True)