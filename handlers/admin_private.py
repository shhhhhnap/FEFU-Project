from keyboards.builerds_kb import get_keyboard

from aiogram.filters import F
from aiogram import Router, Message

from filters.chat_types import ChatTypeFilter, IsAdmin


admin_private_router = Router()
admin_private_router.message.filter(ChatTypeFilter(['private']), IsAdmin())

# Set up the admin routes
admin_KB = get_keyboard(
    'Добавить магазин',
    'Статистика бота',
    'Добавить админа',
    placeholder='Управляй мечтой',
    size=(2)
)


@admin_private_router(F.text == 'Админ')
async def admin_menu(message: Message):
    await message.answer('Что хочешь сделать?', reply_markup=admin_KB)


@admin_private_router(F.text == 'Добавить магазин')
async def add_shop(message: Message):
    await message.answer('Введите название магазина')


@admin_private_router(F.text == 'Статистика бота')
async def stats(message: Message):
    await message.answer('Вот статистика бота: ')


@admin_private_router(F.text == 'Добавить админа')
async def add_admin(message: Message):
    await message.answer('Введите ID админа')