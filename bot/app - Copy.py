from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.start_handler import register_start_handler
from handlers.phone_handler import register_phone_handler
import os

TOKEN = os.getenv("BOT_TOKEN")  # Bot tokenini .env fayldan olish
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Xabar boshqaruvchilari
register_start_handler(dp)
register_phone_handler(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
