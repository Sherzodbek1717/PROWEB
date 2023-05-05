from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_register_button():
    markup = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton("Ro'yxatdan o'tish", callback_data="register")
    markup.add(btn)
    return markup
