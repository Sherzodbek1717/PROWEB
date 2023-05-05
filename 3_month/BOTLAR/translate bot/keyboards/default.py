from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Kantaktni yuborish", request_contact=True)
    markup.add(btn)
    return markup