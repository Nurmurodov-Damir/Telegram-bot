from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database.models import save_user_phone

phone_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
phone_keyboard.add(KeyboardButton("Telefon raqamimni yuborish", request_contact=True))

async def request_phone(message: types.Message):
    await message.answer("Iltimos, telefon raqamingizni yuboring:", reply_markup=phone_keyboard)

async def receive_phone(message: types.Message):
    if message.contact:
        user_id = message.from_user.id
        phone_number = message.contact.phone_number
        await save_user_phone(user_id, phone_number)
        await message.answer("Rahmat, telefon raqamingiz saqlandi!")
    else:
        await message.answer("Iltimos, telefon raqamingizni yuboring!")

def register_phone_handler(dp: Dispatcher):
    dp.register_message_handler(request_phone, commands="sendphone")
    dp.register_message_handler(receive_phone, content_types=["contact"])
