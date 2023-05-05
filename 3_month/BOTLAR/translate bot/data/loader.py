from telebot import TeleBot
from config import TOKEN
from database.database import Database

bot = TeleBot(TOKEN, parse_mode='html')
db = Database("main.db")