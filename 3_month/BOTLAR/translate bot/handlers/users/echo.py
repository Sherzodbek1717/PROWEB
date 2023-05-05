from telebot.types import Message

from data.loader import bot

@bot.message_handler()
def echo(message: Message):
    chat_id = message.chat.id
    bot.copy_message(chat_id, chat_id, message.message_id)
