from bot_keyboard.kb import get_keyboard

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет, я твой помощник по экономии денег! :)', reply_markup=get_keyboard(
        'Добавить товар',
        'Список отслеживаемых товаров',
        'Список поддерживаемых магазинов',
        placeholder='Что вас интересует?',
        sizes=(1, 2)
    ))


@user_private_router.message()
async def other(message: Message):
    await message.answer('Не понимаю тебя.')