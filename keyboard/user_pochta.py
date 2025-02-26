from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choose_line_pochta = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Namangandan Toshkentga 🚙"),
            KeyboardButton(text="Toshkentdan Namanganga 🚙")
        ]
    ],resize_keyboard=True
)

