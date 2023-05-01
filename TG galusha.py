import telebot
from telebot import types
token='6156584613:AAGUcs0iNrdupKLh3IugnsUF6Gmnx7Wl7EY'
bot = telebot.TeleBot('6156584613:AAGUcs0iNrdupKLh3IugnsUF6Gmnx7Wl7EY')
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_poling()
