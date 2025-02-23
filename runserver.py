from mybot.loader import dp, db_manager
from aiogram import executor
import mybot.handlers  # Register handlers
from aiogram import Bot

from aiogram import Bot, Dispatcher, executor, types
import asyncio

BOT_TOKEN = "7856380433:AAGvb5ELa6v6EJGrpubNW5UemRXFkz11kPw"

BOT_ID = None

bot: Bot = Bot(token=BOT_TOKEN)

# Startup function
async def on_startup(_, dispatcher = None):
    print("Bot is running...")
    # db_manager.delete_all_users()
    # db_manager.create_table()
    # db_manager.delete_table()
    db_manager.create_orders_table()
    db_manager.create_users_table()

    global BOT_ID
    me = await bot.get_me()
    BOT_ID = me.id
    print(f"Bot is running... My ID is {BOT_ID}")

@dp.message_handler(lambda msg: msg.text == "check_id")
async def check_bot_id(message: types.Message):
    if BOT_ID:
        await message.reply(f"My ID is {BOT_ID}")
    else:
        await message.reply("Bot ID not set yet.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

