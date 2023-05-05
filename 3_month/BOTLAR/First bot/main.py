from telebot import TeleBot
from telebot.types import Message

# doim iwlaydi
# bot.polling()
# bot.set_webhook() user murojat qilganda iwlaydi halos

bot = TeleBot('5884466659:AAH_mCSfw0XntpUEHu11bMdO92D-V9T4DNQ')


@bot.message_handler(commands=['start', 'help'])
def welcome(message: Message):
    chat_id = -947464471
    chat_id = -856443424
    from_user_id = message.from_user.id
    print(message)
    bot.send_message(chat_id, f"Salom, qondayee {message.from_user.username}?")
    text = f"Botga habar yuborildi!!!" \
           f"Yuboruvci: @{message.from_user.username}"

    bot.copy_message(chat_id, from_user_id, message.message_id)
    bot.send_message(chat_id, text)

@bot.message_handler(content_types=['photo', 'animation', 'sticker', 'video', 'audio', 'voice'])
def reaction_to_types(message: Message):
    chat_id = -947464471
    chat_id = -856443424
    from_user_id = message.from_user.id

    text = f"Botga habar yuborildi!!!" \
           f"Yuboruvci: @{message.from_user.username}"

    bot.copy_message(chat_id, from_user_id, message.message_id)
    bot.send_message(chat_id, text)


# parametr qabul qilgan narsa argument deyiladi


@bot.message_handler(content_types=['text'])
def reaction_to_types(message: Message):
    # print(message)
    chat_id = -856443424
    from_user_id = message.from_user.id
    chat_id = -947464471
    text = f"Botga habar yuborildi!!!" \
           f" Yuboruvci: @{message.from_user.username}"

    bot.copy_message(chat_id, from_user_id, message.message_id)
    bot.send_message(chat_id, text)

bot.infinity_polling()
