from loader import dp,bot
from aiogram import types,F
from aiogram.filters import CommandStart
from aiogram import html
from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
from utils.misc.subscription import check
from aiogram.filters.callback_data import CallbackData
import os
class CheckSubs(CallbackData,prefix='ikb3'):
    check:bool
@dp.message(CommandStart())
async def start_chat(message:types.Message):
   await message.answer(f"Assalomu aleykum, {message.from_user.first_name}")