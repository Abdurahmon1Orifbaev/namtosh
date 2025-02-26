import logging
from aiogram import Bot, Dispatcher, executor
from mybot.loader import dp, db_manager
from mybot import handlers  # Ensure handlers are registered
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found. Make sure it's set in Railway environment variables.")

# Startup function
async def on_startup(dispatcher: Dispatcher):
    logging.info("🚀 Bot is starting up...")
    try:
        db_manager.create_users_table()
        db_manager.create_orders_table()
        db_manager.create_pochta_table()
        logging.info("✅ Database tables created successfully.")
    except Exception as e:
        logging.error(f"❌ Database setup error: {e}")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("🔄 Initializing bot...")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
