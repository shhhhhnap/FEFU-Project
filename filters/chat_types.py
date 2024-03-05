"""
This module contains two classes: ChatTypeFilter and IsAdmin.

ChatTypeFilter is a custom filter that can be used to filter messages based on the type of chat they were sent in.
The constructor takes a list of allowed chat types as its argument. The filter will allow a message through if its chat type is present in the allowed list.

IsAdmin is a custom filter that can be used to filter messages based on whether the sender is an administrator of the chat.
The filter uses the bot instance passed to it to retrieve the list of administrators from the chat. The filter will allow a message through if the sender's ID is present in the list of administrators.
"""

from aiogram.filters import Filter
from aiogram import Bot, types


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        """
    This class represents a custom filter that can be used to filter messages based on the type of chat they were sent in.

    Parameters:
    chat_types (list[str]): A list of allowed chat types. The filter will allow a message through if its chat type is present in this list.

    Usage:
    >>> filter = ChatTypeFilter(['private', 'group'])
    >>> messages = await bot.get_updates(filters=filter)
    """

        self.chat_types = chat_types

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types


class IsAdmin(Filter):
    """
    This class represents a custom filter that can be used to filter messages based on whether the sender is an administrator of the chat.

    Usage:
    >>> filter = IsAdmin()
    >>> messages = await bot.get_updates(filters=filter)
    """

    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message, bot: Bot) -> bool:
        return message.from_user.id in bot.my_admins_list