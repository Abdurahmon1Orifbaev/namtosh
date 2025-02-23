from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
user_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Haydovchi 🚖"),
            KeyboardButton(text="Yo`lovchi 👨‍🦳"),
        ],
        [
            KeyboardButton(text="Ma`lumot 📰")
        ]
    ],resize_keyboard=True
)

choose_line = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Namangandan Toshkentga 🛣"),
            KeyboardButton(text="Toshkentdan Namanganga 🛣")
        ]
    ],resize_keyboard=True
)

orders_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 ta odam 🧍"),
            KeyboardButton(text="3 ta odam 🧍"),
        ],
        [
            KeyboardButton(text="2 ta odam 🧍"),
            KeyboardButton(text="Bo`sh moshina 🚖"),
        ],
        [
            KeyboardButton(text="Back ⬅️"),
        ]
    ],resize_keyboard=True
)

def get_known():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Olish", callback_data="1"))
    keyboard.add(InlineKeyboardButton("Otkaz", callback_data="2"))
    return keyboard


