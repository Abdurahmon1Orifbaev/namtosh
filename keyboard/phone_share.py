from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☎️ Telefon raqamni jo'natish", request_contact=True)
        ]
    ], resize_keyboard=True
)

phone_number_share_pochta = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="☎️ Telefon raqamni jo'natish", request_contact=True)
        ]
    ], resize_keyboard=True
)