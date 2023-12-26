import telebot
from telebot.types import Message
BOT_TOKEN='6740127724:AAEE8oDpajZu0NMRN2h4xLD98XVSQ1leyZ0'
bot=telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start_handler(msg:Message):
    bot.send_message(msg.chat.id,"uyishi botga hush kelibsiz")