from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.states import Shop, DeleteShop
from parsers.dvsota  import dvsota_parser
from parsers.domotekhnika import domotekhnika_parser
from botbd.bd import BotDB


shops_private_router = Router()

db = BotDB('accountant.db')

@shops_private_router.message(F.text == 'Добавить товар')
async def begin(message: Message, state: FSMContext):
    await message.answer('Введите ссылку на товар')
    await state.set_state(Shop.url)

@shops_private_router.message(Shop.url, F.text.startswith('https://'))
async def shop(message: Message, state: FSMContext):
    await state.update_data(url=message.text)
    data = await state.get_data()
    await message.answer(f'Товар успешно принят в обработку!')
    shop_name = data.get('url')
    try:
        if not(db.product_exists(shop_name)): 
            if shop_name.startswith('https://dvsota.ru/'):
                product_name, product_price = dvsota_parser(shop_name)
                db.add_product(message.from_user.id, product_name, product_price, shop_name)
                await message.answer(f'Товар "{product_name}" успешно добавлен!')
            elif shop_name.startswith('https://domotekhnika.ru/'):
                product_name, product_price = domotekhnika_parser(shop_name)
                db.add_product(message.from_user.id, product_name, product_price, shop_name)
                await message.answer(f'Товар "{product_name}" успешно добавлен!')
        else:
            await message.answer(f'Такой товар уже отслеживается!')
    except:
        await message.answer(f'Ошибка при добавлении товара "{shop_name}"')
    await state.clear()


@shops_private_router.message(F.text == 'Удалить товар')
async def cancel(message: Message, state: FSMContext):
    await message.answer('Введите название товара, который хотите удалить.')
    await state.set_state(DeleteShop.delete_shop)

@shops_private_router.message(DeleteShop.delete_shop)
async def delete_shop(message: Message, state: FSMContext):
    await state.update_data(delete_shop=message.text)
    data = await state.get_data()
    product_name = data.get('delete_shop')
    try:
        db.cursor.execute("DELETE FROM usersTG WHERE product_name = ?", (product_name,))
        db.conn.commit()
    except:
        await message.answer(f'Ошибка при удалении товара "{product_name}"')
    await message.answer(f'Товар "{product_name}" успешно удален!')
    await state.clear()





    

