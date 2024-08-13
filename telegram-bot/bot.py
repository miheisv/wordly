import json
from random import randint

import telebot
from requests import get
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from game.game import Game

TOKEN = '7341298603:AAEDIJwQrQad_Ld58oExcTJDGhvG_1eYOs0'
URL = 'http://127.0.0.1:8000'
bot = telebot.TeleBot(TOKEN)
games = dict()
keyboards = dict()

keyboards['start'] = ReplyKeyboardMarkup(resize_keyboard=True)
keyboards['start'].add(KeyboardButton('Меню'))

keyboards['menu'] = ReplyKeyboardMarkup(resize_keyboard=True)
keyboards['menu'].add(KeyboardButton('Игра'))

keyboards['rules'] = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboards['rules'].add(KeyboardButton('Понятно, начинаем!'))


@bot.message_handler(commands=['help', 'start', 'menu'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет -> меню', reply_markup=keyboards['start'])


@bot.message_handler(regexp=r'меню')
def menu_message(message):
    bot.send_message(message.chat.id, 'Меню', reply_markup=keyboards['menu'])


@bot.message_handler(regexp='игра')
def rule_message(message):
    bot.send_message(message.chat.id, 'Правила игры', reply_markup=keyboards['rules'])


@bot.message_handler(regexp='понятно, начинаем!')
def start_game(message):
    word_id = randint(1, json.loads(get(f'{URL}/words_count').content)["words_count"])
    games[message.chat.id] = Game(message.chat.id,
                                1,
                                json.loads(get(f'{URL}/word/{word_id}').content)["word"])
    bot.send_message(message.chat.id, 'Итак, слово загадано!')


@bot.message_handler()
def say_message(message):
    if games.get(message.chat.id, False):
        answer = games.get(message.chat.id).get_answer(message.text)
        bot.send_message(message.chat.id, answer, parse_mode='MarkdownV2')


bot.infinity_polling()
