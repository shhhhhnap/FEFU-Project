from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

shops_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='DNS', url='https://www.dns-shop.ru/'),
        InlineKeyboardButton(text='DVSOTA', url='https://dvsota.ru/'),
        InlineKeyboardButton(text='DOMOTEKHNIKA', url='https://domotekhnika.ru/')
    ]
]
)