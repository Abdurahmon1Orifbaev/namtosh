from aiogram import types
from mybot.loader import dp, bot
from keyboard.user_keyboard import get_known
order_cache = {}
@dp.callback_query_handler(lambda call: call.data == "1")
async def callback_accept(call: types.CallbackQuery):
    msg_id = call.message.message_id
    if msg_id not in order_cache:
        full_info = "Siz zakazni oldingiz"
        try:
            await bot.send_message(
                chat_id=call.from_user.id,
                text=full_info
            )
            await call.answer("Siz zakazni oldingiz", show_alert=True)
        except Exception as e:
            await call.answer("Xatolik yuz berdi: " + str(e), show_alert=True)
    else:
        await call.answer("Bu buyurtmaga allaqachon javob berilgan.", show_alert=True)

@dp.callback_query_handler(lambda call: call.data == "2")
async def callback_decline(call: types.CallbackQuery):
    msg_id = call.message.message_id
    if msg_id in order_cache:
        order = order_cache[msg_id]
        order["decline_count"] += 1
        if order["decline_count"] == 1:
            await call.answer("Siz buyurtmani rad etdingiz. Kuting...", show_alert=True)
        elif order["decline_count"] == 2:
            try:
                await bot.send_message(
                    chat_id=call.from_user.id,
                    text=order["full_info"],
                    reply_markup=get_known()
                )
                await call.answer("Siz zakazni oldingiz", show_alert=True)
                order_cache.pop(msg_id)
            except Exception as e:
                await call.answer("Xatolik yuz berdi: " + str(e), show_alert=True)
        elif order["decline_count"] >= 3:
            order_cache.pop(msg_id)
            await call.answer("Buyurtma bekor qilindi", show_alert=True)
    else:
        await call.answer("Bu buyurtmaga allaqachon javob berilgan.", show_alert=True)


