from aiogram.fsm.state import StatesGroup, State

class Shop(StatesGroup):
    url = State()

class DeleteShop(StatesGroup):
    delete_shop = State()

