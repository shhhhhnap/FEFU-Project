"""
This file contains the main function that starts the bot.

The code is structured as follows:
1. Import statements
2. Global variables and constants
3. Main function

The main function is structured as follows:
1. Delete the webhook and disable polling
2. Start the dispatcher
3. Wait for the user to exit the program

Note: The code assumes that the handlers have been defined in separate files are imported into this file.
"""

# Import statements
from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv
from handlers.user_private import user_private_router
from handlers.admin_private import admin_private_router

# Global variables and constants
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
bot.my_admins_list = []

dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(admin_private_router)


async def main():
    """
    This function deletes the webhook and disables polling, and then starts the dispatcher.
    """
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    """
    This block of code executes when the program is run directly from the command line.
    It calls the main function, and waits for the user to exit the program.
    """
    asyncio.run(main())
