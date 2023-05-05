from data.loader import bot
from telebot.types import Message


@bot.message_handler(commands=['start'])
def welcome(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu alaykum, {message.from_user.full_name} " 
                              f"wikipediya botiga xush kelibsiz!")





