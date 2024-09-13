from loader import dp
from aiogram.filters import CommandStart
from aiogram import types
@dp.message(CommandStart())
async def start(message:types.Message):
   await message.answer(f"Assalomu aleykum, {message.from_user.first_name}")