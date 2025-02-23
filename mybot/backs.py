from aiogram import types
from aiogram.dispatcher import FSMContext

from mybot.loader import dp
from keyboard.user_keyboard import user_menu


@dp.message_handler(text="Back ⬅️", state="*")
async def stickers_menu(message: types.Message, state: FSMContext):
    text = "Botni 1 sahifasiga o`tdingiz"
    await message.answer(text=text, reply_markup=user_menu)
    await state.finish()