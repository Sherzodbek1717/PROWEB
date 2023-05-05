# import logging
#
# from aiogram import Bot, Dispatcher, executor, types
#
# API_TOKEN = '6239607197:AAHj3OviTFfU0cqT6FWC80Y2udCvs_AAnUc'
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Salom!\nI'm Wikipediya Bot!\nPowered by https://t.me/sherzodbek1717.")
#
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)
#     if __name__ == '__main__':
#         executor.start_polling(dp, skip_updates=True)


"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6239607197:AAHj3OviTFfU0cqT6FWC80Y2udCvs_AAnUc'
wikipedia.set_lang('uz')


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
