import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties

import asyncio

from handlers.user_private import user_private_router

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')


async def main():
    dp = Dispatcher()
    dp.include_router(user_private_router)
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    



if __name__ == '__main__':
    asyncio.run(main())
