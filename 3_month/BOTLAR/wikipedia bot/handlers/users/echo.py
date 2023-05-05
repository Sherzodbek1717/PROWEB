from data.loader import bot
from telebot.types import Message

@bot.message_handler(content_types=['text', 'audio', 'video', 'sticker', 'photo', 'animation'])
def echo(message: Message):
    chat_id = message.from_user.id
    bot.copy_message(chat_id, chat_id, message.message_id)