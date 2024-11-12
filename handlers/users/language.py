from loader import dp,db
from aiogram.filters import Command
from aiogram import types, F
from keyboards.inline.buttons import btn

# Foydalanuvchining tiliga qarab mos xabarni qaytaradigan funksiya
def get_language_message(language='en'):
    messages = {
        'en': "Which language would you like to use?",
        'ru': "На каком языке вы хотите получить информацию?",
        'uz': "Qaysi tilda ma'lumot olishni istaysiz?"
    }
    # Tanlangan til bo'yicha xabarni qaytaradi, agar topilmasa, default bo'lib ingliz tili qaytadi
    return messages.get(language, messages['en'])

@dp.message(Command("language"))
async def language(message:types.Message):
    # foydalanuvchining id sini olish
    user_id = message.from_user.id
    # foydalanuvchining tilini ma'lumotlar bazasidan olish
    language = db.get_user_language(user_id)
    # Foydalanuvchiga til tanlash uchun xabar yuboramiz va inline tugmalarni jo'natamiz
    await message.reply(text=get_language_message(language), # hozirgi tilga mos xabar
                        reply_markup=btn(language=language) # Til tanlash uchun inline klaviaturani yuboramiz
    )

# Inline tugmalardan birini tanlaganda keladigan callback query uchun handler
@dp.callback_query(F.data.in_(['en','ru','uz'])) # Faqat kerakli tillar uchun ishlaydi
async def language_callback_query(call:types.CallbackQuery):
    # foydalanuvchi id sini olish
    user_id = call.from_user.id
    # foydalanuvchi tanlagan tilni olish
    select_language = call.data

    # Foydalanuvchining tilini ma'lumotlar bazasida yangilash
    db.update_user_language(select_language,user_id)

    # Tanlangan tilga mos ravishda tasdiqlovchi xabarni tayyorlaymiz
    language_message = {
        'en': "Language set to English",
        'ru': "Язык установлен на Русский",
        'uz': "Til O'zbek tiliga sozlandi"
    }.get(select_language, "Unknown language")

    # Callback query-ga javob yuborish, caching vaqti 60 soniya
    await call.answer(cache_time=60)
    # Foydalanuvchiga yangi xabar yuborish (til o'zgarganini bildirish)
    await call.message.edit_text(language_message)