from aiogram import Router,F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


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


@router.message(F.text=='Правила')
async def rules(message: Message):
    await message.answer(
        "Скоро буде :)",
    )

@router.message()
async def checker(message:Message):
    await message.reply('Я вас не зрозумів :(')
