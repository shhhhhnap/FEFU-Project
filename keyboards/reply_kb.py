from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

start_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Добавить товар')
    ],
    [
        KeyboardButton(text='Список отслеживаемых товаров')
    ],
    [
        KeyboardButton(text='Список поддерживаемых магазинов')
    ]
],
    resize_keyboard=True
)