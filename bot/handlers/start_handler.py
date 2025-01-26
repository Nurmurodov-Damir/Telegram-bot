from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command
from .utils import check_subscription

CHANNELS = ["@kanal1", "@kanal2"]

async def start_command(message: types.Message):
    user_id = message.from_user.id
    bot = message.bot

    if not await check_subscription(user_id, bot, CHANNELS):
        text = "Quyidagi kanallarga obuna bo‘ling:\n"
        text += "\n".join([f"- {channel}" for channel in CHANNELS])
        text += "\n\n✅ Obuna bo‘lgach, /start buyrug‘ini qaytadan yuboring."
        await message.answer(text)
    else:
        await message.answer("Xush kelibsiz! Iltimos, telefon raqamingizni yuboring /sendphone")

def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, Command("start"))
