from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
def btn(lang='uz'):
    keyboard = InlineKeyboardBuilder()
    text = {
        'en': ["Translate to English", "Translate to Russian", "Translate to Uzbek"],
        'ru': ["Перевести на английский", "Перевести на русский", "Перевести на узбекский"],
        'uz': ["Ingliz tiliga tarjima", "Rus tiliga tarjima", "O'zbek tiliga tarjima"]
    }
    buttons = [
        InlineKeyboardButton(text=text.get(lang, [])[0], callback_data="en"),
        InlineKeyboardButton(text=text.get(lang, [])[1], callback_data="ru"),
        InlineKeyboardButton(text=text.get(lang, [])[2], callback_data="uz")
    ]
    keyboard.add(*buttons)
    keyboard.adjust(1)  # Tugmalarni bitta qatorga joylashtirish
    return keyboard.as_markup()