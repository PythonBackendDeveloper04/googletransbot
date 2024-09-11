from loader import dp
from aiogram import types,F
from aiogram.filters import Command
from handlers.users.language import user_languages
import os
from googletrans import Translator
from gtts import gTTS
@dp.message(F.text)
async def translate(message:types.Message):
    user_id = message.from_user.id
    lang = user_languages.get(user_id,'en')
    tarjimon = Translator()
    try:
        tarjima = tarjimon.translate(message.text, dest=lang)
        await message.answer(tarjima.text)
        if lang != 'uz':
            tts = gTTS(tarjima.text, lang=lang)
            tts.save(f'{message.chat.id}.mp3')
            file = types.input_file.FSInputFile(path=f"{message.chat.id}.mp3")
            await message.answer_voice(voice=file)
        else:
            pass
        try:
            os.remove(f'{message.chat.id}.mp3')
        except:
            pass
    except:
        await message.answer("So'zning to'g'ri yozilganiga ishonch hosil qiling")