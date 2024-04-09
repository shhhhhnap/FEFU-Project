"""
This file contains the main code for the bot.

It sets up the Aiogram bot and its routes,
and defines the behavior of the different commands.
"""

from aiogram import types, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards import reply_kb
from keyboards import inline_kb
from botbd.bd import BotDB


from utils.states import Shop

user_private_router = Router()

db = BotDB('accountant.db')


@user_private_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')
    await message.answer('Я твой персональный помощник по экономии денег, скорее нажми кнопку "Начать".', reply_markup=reply_kb.start_kb)


@user_private_router.message(F.text == 'Начать')
async def begin(message: types.Message):
    await message.answer('Вот список функций:', reply_markup=reply_kb.functions_kb)

@user_private_router.message(F.text == 'Список поддерживаемых магазинов')
async def shops(message: types.Message):
    await message.answer(f'Вот список поддерживаемых магазинов:', reply_markup=inline_kb.shops_kb)

@user_private_router.message(F.text == 'Список ваших товаров')
async def items_list(message: types.Message):
    db.cursor.execute("SELECT product_name FROM usersTG WHERE telegramID = ?", (message.from_user.id,))
    if len(db.cursor.fetchall()) < 1:
        await message.answer(f'Вы еще не добавили ни одного товара.')
    else:
        await message.answer(f'Вот список ваших товаров:')
        db.cursor.execute('SELECT product_name FROM usersTG WHERE telegramID = ?', (message.from_user.id,))
        items = db.cursor.fetchall()
        user_items = [str(*item) for item in items]
        for index, value in enumerate(user_items, 1):
            await message.answer(f'{index}. {value}')

