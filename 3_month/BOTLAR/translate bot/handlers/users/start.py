from telebot.types import Message

from data.loader import bot, db
from keyboards.inline import get_register_button


@bot.message_handler(commands=['start'], chat_types=['private'])
def start(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    db.insert_telegram_id(from_user_id)
    check = db.check_user(from_user_id)
    if None in check:
        bot.send_message(chat_id, f"Assalomu alaykum, {message.from_user.full_name}\n" 
                                  f"<b>Translate bot</b>ga xush kelibsiz!\n" 
                                  f"Botdan foydalanish uchun avval ro'yhatdan o'ting!",
                         reply_markup=get_register_button())
