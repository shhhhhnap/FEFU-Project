from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_keyboard(
    *btns: str,
    placeholder: str = None,
    sizes: tuple[int]
):
    """
        This function creates a keyboard with the specified buttons.

        Args:
            btns (str): A variable length argument list of strings that will be used as the buttons on the keyboard.
            placeholder (str, optional): A placeholder text that will be displayed in the text input field of the keyboard. Defaults to None.
            sizes (tuple[int]): A tuple of two integers that specify the number of rows and columns of buttons on the keyboard.

        Returns:
            str: A JSON encoded string that represents the keyboard.

        """
    keyboard = ReplyKeyboardBuilder()

    for text in btns:
        keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(resize_keyboard=True,
                                             input_field_placeholder=placeholder)