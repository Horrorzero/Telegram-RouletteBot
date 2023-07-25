from aiogram import Router,F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.handlers.start import router as start_router
from bot.handlers.checker import router as checker_router
from bot.handlers.rules import router as rules_router

router = Router()

router.include_routers(start_router, rules_router,checker_router)

class Game(StatesGroup):
    mode = State()
    color = State()
    num = State()
    

@router.message(F.text=='Грати')
async def play(message: Message, state: FSMContext):
    await message.answer('hello')