import random
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from game import Game

# from static_dev import TELEGRAM_TOKEN - для реальной работы
# from static_dev import TELEGRAM_TOKEN  # DEV-режим


TOKEN = '7341298603:AAEDIJwQrQad_Ld58oExcTJDGhvG_1eYOs0'
URL = 'https://geek-jokes.sameerkumar.website/api?format=json'
bot = telebot.TeleBot(TOKEN)

keyboards = dict()

keyboards['start'] = ReplyKeyboardMarkup(resize_keyboard=True)
keyboards['start'].add(KeyboardButton('Меню'))

keyboards['menu'] = ReplyKeyboardMarkup(resize_keyboard=True)
keyboards['menu'].add(KeyboardButton('Игра'))

keyboards['rules'] = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboards['rules'].add(KeyboardButton('Понятно, начинаем!'))

games = dict()
words = ['парта', 'выдра', 'уголь', 'рыжик', 'пирог', 'рукав', 'порка', 'спина', 'длань']


@bot.message_handler(commands=['help', 'start', 'menu'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет -> меню', reply_markup=keyboards['start'])


@bot.message_handler(regexp=r'меню')
def say_message(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=keyboards['menu'])


@bot.message_handler(regexp='игра')
def say_message(message):
    bot.send_message(message.chat.id, 'Правила игры', reply_markup=keyboards['rules'])


@bot.message_handler(regexp='понятно, начинаем!')
def say_message(message):
    # здесь создаем игру
    games[message.chat.id] = Game(message.chat.id, 1, random.choice(words))
    bot.send_message(message.chat.id, 'Итак, слово загадано!')


@bot.message_handler()
def say_message(message):
    # идет игра
    if games.get(message.chat.id, False):
        answer = games.get(message.chat.id).get_answer(message.text)
        bot.send_message(message.chat.id, answer, parse_mode='MarkdownV2')


bot.infinity_polling()
