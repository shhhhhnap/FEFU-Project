import os

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv, find_dotenv
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, types, F

import asyncio

from handlers.user_private import user_private_router
from handlers.shops import shops_private_router


async def main():
    load_dotenv(find_dotenv())
    bot_token = os.getenv('BOT_TOKEN')
    dp = Dispatcher()
    dp.include_routers(user_private_router, shops_private_router)
    bot = Bot(bot_token)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
