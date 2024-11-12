from loader import dp,db
from aiogram.filters import CommandStart
from aiogram import types
@dp.message(CommandStart())
async def start(message:types.Message):
   try:
      db.add_user(fullname=message.from_user.full_name, telegram_id=message.from_user.id)
   except Exception as e:
      print(e)
   text = """
   🇺🇿 Xush kelibsiz {}!
Botimizdan foydalanish uchun /language buyrugi orqali tilni tanlang
Til tanlanmagan holatda matnlar avtomatik barcha tillarda Ingliz tiliga tarjima qilinadi

🇺🇸 Welcome {}!
To use the bot, please choose a language via the /language command
If no language is selected, texts will be automatically translated to English from all languages

🇷🇺 Добро пожаловать, {}!
Для использования бота выберите язык с помощью команды /language
Если язык не выбран, тексты будут автоматически переведены на английский язык из всех остальных языков>
   """.format(message.from_user.first_name,message.from_user.first_name,message.from_user.first_name)
   await message.answer(text=text)