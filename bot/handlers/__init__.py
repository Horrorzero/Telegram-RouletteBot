from aiogram import Router,F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bot.handlers.start import router as start_router
from bot.handlers.checker import router as checker_router
from bot.handlers.rules import router as rules_router

from bot.keyboard.game_keyboard import get_game_inline_markup
from bot.keyboard.color_keyboard import get_color_inline_markup

router = Router()

router.include_routers(start_router, rules_router,checker_router)

class Game(StatesGroup):
    color = State()
    num = State()
    money = State()
    

@router.message(F.text=='Грати')
async def play(message: Message):
    game_markup = get_game_inline_markup()
    lines = [
        'Оберіть режим:',
        '1.Обрати колір і число',
        '2.Обрати тільки колір',
        '3.Обрати тільки число',
        '4.Обрати два кольори і два числа',
    ]
    await message.answer(
        text='\n'.join(lines),
        reply_markup=game_markup
    )


@router.callback_query(lambda query: query.data == '1')
async def color(callback: CallbackQuery, state: FSMContext):
    color_markup = get_color_inline_markup()

    await state.set_state(Game.color)
    await callback.message.answer(
        text='Оберіть колір',
        reply_markup=color_markup
    )

    @router.callback_query(lambda query: query.data == 'col_black')
    async def num(callback:CallbackQuery, state:FSMContext):
        await state.update_data(color=callback.data)
        await state.set_state(Game.num)

        lines = [
            'Оберіть число',
            'Введіть будь яке число від 1 до 36',
        ]

        await callback.message.answer(
            text='\n'.join(lines)
        )

    @router.message(Game.num)
    async def money(message:Message,state:FSMContext):
        await state.update_data(num=message.text)
        await state.set_state(Game.money)

        await message.answer(
            text='Введіть вашу ставку:'
        )

    @router.message(Game.money)
    async def success(message:Message,state:FSMContext):
        await state.update_data(money=message.text)

        lines = [
            'Ваша ставка прийнята',
            'Зачекайте декілька секунд',
        ]

        await message.answer(
            text='\n'.join(lines)
        )

@router.callback_query(lambda query: query.data == '2')
async def color(callback: CallbackQuery, state: FSMContext):
    color_markup = get_color_inline_markup()

    await state.set_state(Game.color)
    await callback.message.answer(
        text='Оберіть колір',
        reply_markup=color_markup
    )

    @router.callback_query(lambda query: query.data == 'col_black')
    async def num(callback:CallbackQuery, state:FSMContext):
        await state.update_data(color=callback.data)
        await state.set_state(Game.num)

        lines = [
            'Оберіть число',
            'Введіть будь яке число від 1 до 36',
        ]

        await callback.message.answer(
            text='\n'.join(lines)
        )

    @router.message(Game.num)
    async def money(message:Message,state:FSMContext):
        await state.update_data(num=message.text)
        await state.set_state(Game.money)

        await message.answer(
            text='Введіть вашу ставку:'
        )

    @router.message(Game.money)
    async def success(message:Message,state:FSMContext):
        await state.update_data(money=message.text)

        lines = [
            'Ваша ставка прийнята',
            'Зачекайте декілька секунд',
        ]

        await message.answer(
            text='\n'.join(lines)
        )

@router.callback_query(lambda query: query.data == '3')
async def color(callback: CallbackQuery, state: FSMContext):
    color_markup = get_color_inline_markup()

    await state.set_state(Game.color)
    await callback.message.answer(
        text='Оберіть колір',
        reply_markup=color_markup
    )

    @router.callback_query(lambda query: query.data == 'col_black')
    async def num(callback:CallbackQuery, state:FSMContext):
        await state.update_data(color=callback.data)
        await state.set_state(Game.num)

        lines = [
            'Оберіть число',
            'Введіть будь яке число від 1 до 36',
        ]

        await callback.message.answer(
            text='\n'.join(lines)
        )

    @router.message(Game.num)
    async def money(message:Message,state:FSMContext):
        await state.update_data(num=message.text)
        await state.set_state(Game.money)

        await message.answer(
            text='Введіть вашу ставку:'
        )

    @router.message(Game.money)
    async def success(message:Message,state:FSMContext):
        await state.update_data(money=message.text)

        lines = [
            'Ваша ставка прийнята',
            'Зачекайте декілька секунд',
        ]

        await message.answer(
            text='\n'.join(lines)
        )

@router.callback_query(lambda query: query.data == '4')
async def color(callback: CallbackQuery, state: FSMContext):
    color_markup = get_color_inline_markup()

    await state.set_state(Game.color)
    await callback.message.answer(
        text='Оберіть колір',
        reply_markup=color_markup
    )

    @router.callback_query(lambda query: query.data == 'col_black')
    async def num(callback:CallbackQuery, state:FSMContext):
        await state.update_data(color=callback.data)
        await state.set_state(Game.num)

        lines = [
            'Оберіть число',
            'Введіть будь яке число від 1 до 36',
        ]

        await callback.message.answer(
            text='\n'.join(lines)
        )

    @router.message(Game.num)
    async def money(message:Message,state:FSMContext):
        await state.update_data(num=message.text)
        await state.set_state(Game.money)

        await message.answer(
            text='Введіть вашу ставку:'
        )

    @router.message(Game.money)
    async def success(message:Message,state:FSMContext):
        await state.update_data(money=message.text)

        lines = [
            'Ваша ставка прийнята',
            'Зачекайте декілька секунд',
        ]

        await message.answer(
            text='\n'.join(lines)
        )
