"""
This Example will show you how to use register_next_step handler.
"""

import telebot
from telebot import types

API_TOKEN = '5393292456:AAHe6eYVty2SWs4h-9GeMDjzgMMeowMcPLE'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.jk = None


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Laki-laki', 'Perempuan')
    msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
    bot.register_next_step_handler(msg, func_usia)


def func_usia(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female')
        msg = bot.reply_to(message, 'What is your gender')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(
                message, 'Age should be a number. How old are you?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female')
        msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
        bot.register_next_step_handler(msg, func_usia)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def func_usia(message):
    try:
        chat_id = message.chat.id
        jk = message.text
        user = user_dict[chat_id]
        if (jk == u'Male') or (jk == u'Female'):
            user.jk = jk
        else:
            raise Exception("Unknown jk")
        bot.send_message(chat_id, 'Nice to meet you ' + user.name +
                         '\n Age:' + str(user.age) + '\n Sex:' + user.jk)
    except Exception as e:
        bot.reply_to(message, 'oooops')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.infinity_polling()
