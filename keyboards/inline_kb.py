from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

shops_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='DVSOTA', url='https://dvsota.ru/'),
        InlineKeyboardButton(text='DOMOTEKHNIKA', url='https://domotekhnika.ru/')
    ]
]
)