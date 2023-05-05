# from telebot.types import CallbackQuery, Message, ReplyKeyboardRemove
#
# from data.loader import bot, db
# from keyboards.default import send_contact
#
# data = {}
# @bot.callback_query_handler(func=lambda call: call.data == 'register')
# def registration(call: CallbackQuery):
#     print(call)
#     chat_id = call.message.chat.id
#     from_user_id = call.from_user.id
#     bot.delete_message(chat_id, call.message.message_id)
#     bot.send_message(chat_id, "Telefon no'meringizni yuboring!", reply_markup=send_contact())
#     bot.register_next_step_handler(msg, reaction_to_contact)
#
# def reaction_to_contact(message: Message):
#     chat_id = message.chat.id
#     from_user_id = message.from_user.id
#     phone_number = message.contact.phone_number
#     data[from_user_id] = {
#         "phone_number": phone_number
#     }
#     msg = bot.send_message(chat_id, "Ismingizni kiriting", reply_markup=ReplyKeyboardRemove())
#     bot.register_next_step_handler(msg, save_user)
#
# def save_user(message: Message):
#     chat_id = message.chat.id
#     from_user_id = message.from_user.id
#
#     data[from_user_id]['name'] = message.text
#
#     user_name = data[from_user_id]['name']
#     phone_number = data[from_user_id]['phone_number']

from telebot.types import CallbackQuery, Message, ReplyKeyboardRemove

from data.loader import bot, db
from keyboards.default import send_contact

data = {}

@bot.callback_query_handler(func=lambda call: call.data == 'register')
def registration(call: CallbackQuery):
    # print(call)
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    bot.delete_message(chat_id, call.message.message_id)
    msg = bot.send_message(chat_id, "Telefon no'meringizni yuboring!", reply_markup=send_contact())
    bot.register_next_step_handler(msg, reaction_to_contact)

def reaction_to_contact(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    phone_number = message.contact.phone_number
    data[from_user_id] = {
        "phone_number": phone_number
    }
    msg = bot.send_message(chat_id, "Ismingizni kiriting", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, save_user)

def save_user(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    data[from_user_id]['name'] = message.text

    user_name = data[from_user_id]['name']
    phone_number = data[from_user_id]['phone_number']

    print(user_name, phone_number)
