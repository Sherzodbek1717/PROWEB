from data.loader import bot, db
import handlers


db.create_user_table()


if __name__ == '__main__':
    bot.polling(non_stop=True)














