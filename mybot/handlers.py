from aiogram import types
from aiogram.dispatcher import FSMContext
from mybot.loader import dp, db_manager, bot
from keyboard.phone_share import phone_number_share
from keyboard.user_keyboard import user_menu, choose_line, orders_menu, get_known
from state.user_order_state import Register

GROUP_CHAT_ID = -1002457389396

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Botga hush kelibsiz!", reply_markup=user_menu)

@dp.message_handler(text="Haydovchi 🚖")
async def rider_handler(message: types.Message):
    text = """
Agar siz haydovchi bo‘lishni istasangiz, bizning adminimmizga murojaat qiling:
📩 Telegram: @Namtosh7787
📞 Telefon: +999-90-798-77-87
    """
    await message.answer(text)

@dp.message_handler(text="Ma`lumot 📰")
async def about_us(message: types.Message):
    text = """
Admin 👤: @Namtosh7787
Admin(2) 👤: @azamov935
    """
    await message.answer(text)

@dp.message_handler(text="Yo`lovchi 👨‍🦳", state="*")
async def send_orders(message: types.Message, state: FSMContext):
    await message.answer("Yo`nalishni tanlang", reply_markup=choose_line)
    await Register.line.set()

@dp.message_handler(state=Register.line)
async def choosing_line(message: types.Message, state: FSMContext):
    await state.update_data({"line": message.text})
    text = "Iltimos telefon raqamingizni kiriting."
    await message.answer(text, reply_markup=phone_number_share)
    await Register.phone_number.set()

@dp.message_handler(state=Register.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number_state(message: types.Message, state: FSMContext):
    await state.update_data({
        "phone_number": message.contact.phone_number,
        "user_id": message.chat.id
    })
    text = """
Qachon ketishingizni vaxtini kiriting !:
Masalan: Bugun kechqurun soat 16:00 da !
"""
    await message.answer(text=text)
    await Register.time.set()

@dp.message_handler(state=Register.time)
async def time_state(message: types.Message, state: FSMContext):
    await state.update_data({"time": message.text})
    text = "Nechta odam borligini kiriting Yoki pustoy moshinani tanlang"
    await message.answer(text=text, reply_markup=orders_menu)
    await Register.members.set()

order_cache = {}

@dp.message_handler(state=Register.members)
async def count_members(message: types.Message, state: FSMContext):
    await state.update_data({"members": message.text})
    data = await state.get_data()

    text_hidden = f"""
Shaxs: Yo`lovchi
Yo`nalish: {data.get("line")}
Telefon raqam: ❌ Maxfiy
Ketish vohti: {data.get("time")}
Odam soni: {data.get("members")}
"""
    text_full = f"""
Shaxs: Yo`lovchi
Yo`nalish: {data.get("line")}
Telefon raqam: {data.get("phone_number")}
Ketish vohti: {data.get("time")}
Odam soni: {data.get("members")}
"""

    await message.answer(text=text_full)

    sent_msg = await bot.send_message(chat_id=GROUP_CHAT_ID, text=text_hidden)
    order_cache[sent_msg.message_id] = text_full

    confirmation_text = (
        "Sizning zakazingiz muvofiqiyatli bo`ldi. Haydovchilar yozishini kuting ✅"
        if db_manager.append_user(data)
        else "Botda muammo mavjud, biz bilan bog'laning"
    )
    await message.answer(text=confirmation_text, reply_markup=user_menu)
    await state.finish()

@dp.message_handler(
    lambda message: (
        message.reply_to_message is not None
        and message.chat.id == GROUP_CHAT_ID
    ),
    content_types=[types.ContentType.VOICE, types.ContentType.AUDIO]  # Voice or audio messages
)
async def send_full_info_in_pm_voice(message: types.Message):
    replied_msg_id = message.reply_to_message.message_id

    if replied_msg_id in order_cache:
        full_info = order_cache.pop(replied_msg_id)  # Only the first valid reply
        try:
            await bot.send_message(chat_id=message.from_user.id, text=full_info, reply_markup=get_known())
            await message.reply("✅ To'liq ma'lumot shaxsiy xabarga yuborildi.")
        except Exception as e:
            await message.reply(f"❌ Xatolik yuz berdi: {e}")




@dp.message_handler(lambda message: message.reply_to_message and message.chat.id == GROUP_CHAT_ID)
async def debug_handler(message: types.Message):
    print("Content type:", message.content_type)

@dp.message_handler(commands=["get_group_id"])
async def get_group_id(message: types.Message):
    await message.answer(f"Group Chat ID: {message.chat.id}")
