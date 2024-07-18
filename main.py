import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests

# from static_dev import TELEGRAM_TOKEN - для реальной работы
# from static_dev import TELEGRAM_TOKEN  # DEV-режим



TOKEN = '7341298603:AAEDIJwQrQad_Ld58oExcTJDGhvG_1eYOs0'
URL = 'https://geek-jokes.sameerkumar.website/api?format=json'
bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Меню'))


@bot.message_handler(commands=['help', 'start', 'menu', 'привет', 'меню', 'старт'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=keyboard)


@bot.message_handler(regexp=r'меню\.*')
def say_message(message):
    bot.send_message(message.chat.id, 'Меню')


bot.infinity_polling()