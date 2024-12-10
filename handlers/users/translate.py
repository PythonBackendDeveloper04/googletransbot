from loader import dp,db
from aiogram import types,F
from googletrans import Translator # Google Translator API
from gtts import gTTS # Google Text To Speech (gTTS)
import time
import os
@dp.message(F.text)
async def translate(message:types.Message):
    # foydalanuvchining id sini olish
    user_id = message.from_user.id
    # Foydalanuvchining tilini ma'lumotlar bazasidan olish
    language = db.get_user_language(user_id)
    print(language)

    # Translator sinfidan obyekt olamiz
    translator = Translator()
    try:
        # xabar matnini foydalanuvchining tiliga tarjima qilish
        translated = translator.translate(message.text, dest=language)

        # tarjima qilingan matnni foydalanuvchiga yuborish
        await message.answer(translated.text)

        # agar foydalanuvchi tili o'zbekcha bo'lmasa ovozli xabar ham yuboramiz
        if language != 'uz':
            # tarjimani ovozga aylantirish
            tts = gTTS(translated.text, lang=language)
            # Ovozli faylni saqlash (chat ID bilan nomlangan fayl)
            tts.save(f"{message.from_user.id}.mp3")
            # Ovozli faylni yuborish
            file = types.input_file.FSInputFile(path=f"{message.from_user.id}.mp3")
            await message.answer_voice(voice=file)
        else:
            # Agar foydalanuvchining tili o'zbekcha bo'lsa, ovozli xabar yuborilmaydi
            pass
        try:
            # Ovozli faylni o'chirish
            os.remove(f"{message.from_user.id}.mp3")
        except Exception as e:
            # xatolik kelib chiqsa konsolga chiqarish
            print(e)
    except:
        await message.answer("So'zning to'g'ri yozilganligiga ishonch hosil qiling")