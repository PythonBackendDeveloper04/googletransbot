from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
def btn(language='uz'):
    keyboard = InlineKeyboardBuilder()
    # Har bir til uchun tarjima tugmalarining matnlarini saqlash
    text = {
        'en': ["Translate to English", "Translate to Russian", "Translate to Uzbek"],
        'ru': ["Перевести на английский", "Перевести на русский", "Перевести на узбекский"],
        'uz': ["Ingliz tiliga tarjima", "Rus tiliga tarjima", "O'zbek tiliga tarjima"]
    }
    # tugmalar ro'yhati
    buttons = [
        InlineKeyboardButton(text=text.get(language, [])[0], callback_data="en"),
        InlineKeyboardButton(text=text.get(language, [])[1], callback_data="ru"),
        InlineKeyboardButton(text=text.get(language, [])[2], callback_data="uz")
    ]
    # tugmalarni klaviaturaga qo'shish
    keyboard.add(*buttons)

    # tugmalarni bitta ustunda joylashtirish
    keyboard.adjust(1)

    # Klaviaturani markup formatida qaytarish
    return keyboard.as_markup()