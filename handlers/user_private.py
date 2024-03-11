"""
This file contains the main code for the bot.

It sets up the Aiogram bot and its routes,
and defines the behavior of the different commands.
"""

from aiogram import types, F, Router
from aiogram.filters import CommandStart

from sqlitebase import bd
import keyboards

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start(message: types.Message):
    """
This function is triggered when the user sends a message that starts with "/start".
It replies with a greeting message that includes the user's first name and user ID.

Parameters:
    message (types.Message): The incoming message from the user.

Returns:
    None
"""
    await message.answer(f'Привет, {message.from_user.first_name} {message.from_user.id}', reply_markup=keyboards.reply_kb.start_kb)
    

@user_private_router.message(F.text.startswith('https://www.dns-shop.ru'))
async def dns(message: types.Message):
    product_url = message.text
    await message.answer(f'Товар {product_url} успешно добавлен в список.')


@user_private_router.message()
async def other(message: types.Message):
    msg = message.text.lower()
    match msg:
        case 'добавить товар':
            await message.answer(f'Введите ссылку на товар')
        case 'список поддерживаемых магазинов':
            await message.answer(f'<b>Вот поддерживаемые магазины:</b>', reply_markup=keyboards.shops_kb)


