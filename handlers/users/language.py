from loader import dp
from aiogram.filters import Command
from aiogram import types, F
from keyboards.inline.buttons import btn

user_languages = {}

def get_language_message(lang='en'):
    messages = {
        'en': "Which language would you like to use?",
        'ru': "На каком языке вы хотите получить информацию?",
        'uz': "Qaysi tilda ma'lumot olishni istaysiz?"
    }
    return messages.get(lang, messages['en'])

@dp.message(Command("language"))
async def language(message:types.Message):
    user_id = message.from_user.id
    lang = user_languages.get(user_id,'en')
    await message.reply(text=get_language_message(lang), reply_markup=btn(lang=lang))

@dp.callback_query(F.data.in_(['en','ru','uz']))
async def language_callback_handler(call:types.CallbackQuery):
    user_id = call.from_user.id
    select_language = call.data
    user_languages[user_id] = select_language
    language_message = {
        'en': "Language set to English",
        'ru': "Язык установлен на Русский",
        'uz': "Til O'zbek tiliga sozlandi"
    }.get(select_language, "Unknown language")

    await call.answer(cache_time=60)
    await call.message.edit_text(language_message)