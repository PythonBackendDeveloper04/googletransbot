from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
def btn(language='uz'):
    keyboard = InlineKeyboardBuilder()
    text = {
        'en': ["Translate to English", "Translate to Russian", "Translate to Uzbek"],
        'ru': ["Перевести на английский", "Перевести на русский", "Перевести на узбекский"],
        'uz': ["Ingliz tiliga tarjima", "Rus tiliga tarjima", "O'zbek tiliga tarjima"]
    }
    buttons = [
        InlineKeyboardButton(text=text.get(language, [])[0], callback_data="en"),
        InlineKeyboardButton(text=text.get(language, [])[1], callback_data="ru"),
        InlineKeyboardButton(text=text.get(language, [])[2], callback_data="uz")
    ]
    keyboard.add(*buttons)
    keyboard.adjust(1)
    return keyboard.as_markup()