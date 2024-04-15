from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Начать'),
    ]
], resize_keyboard=True
)

functions_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Добавить товар'),
        KeyboardButton(text='Список ваших товаров')
    ],
    [   
        KeyboardButton(text='Удалить товар'),
    ],
    [
        KeyboardButton(text='Список поддерживаемых магазинов'),
    ]
], resize_keyboard=True
)
