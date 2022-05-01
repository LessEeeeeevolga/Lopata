import telebot
import random

bot = telebot.TeleBot('TOKEN HERE')

@bot.message_handler(commands=['start'])
def start_message_response(message):
    bot.send_message(message.chat.id, 'Салам пополам! Вот твое число:')
    number = random.randint(1, 1001)
    bot.send_message(message.chat.id, number)

@bot.message_handler(content_types=['text'])
def any_message_response(message):
    border = int(message.text)
    if border < 1:
        bot.send_message(message.chat.id, 'Брат, я так не умею :(')
        return
    number = random.randint(1, border)
    bot.send_message(message.chat.id, number)

bot.polling()