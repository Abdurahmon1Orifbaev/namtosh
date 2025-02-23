from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import BOT_TOKEN
from utils.db_api.database import DatabaseManager

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

db_manager = DatabaseManager("nam_tosh.db")
