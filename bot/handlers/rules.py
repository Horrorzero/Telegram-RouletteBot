from aiogram import Router,F
from aiogram.types import Message

router = Router()

@router.message(F.text=='Правила')
async def rules(message: Message):
    await message.answer(
        "Скоро буде :)",
    )