from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboard.start_keyboard import get_menu_reply_markup


router = Router()
@router.message(CommandStart())
async def start(message: Message):
    menu_markup = get_menu_reply_markup()
    lines = [
        f"Вітаю, {message.from_user.first_name}.",
        "Я - Roulette Bot, тут Ви можете зіграти в рулетку",
        "Щоб розпочати оберіть опцію з меню"
    ]

    await message.answer(
        text='\n'.join(lines),
        reply_markup=menu_markup
    )
