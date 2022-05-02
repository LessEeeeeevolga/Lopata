import telebot
import random

bot = telebot.TeleBot('TOKEN_HERE')

@bot.message_handler(commands=['start'])
def start_message_response(message):
    bot.send_message(message.chat.id, 'Салам пополам! Вот твое число:')
    number = random.randint(1, 1001)
    bot.send_message(message.chat.id, number)

@bot.message_handler(content_types=['text'])
def any_message_response(message):
    if message.text.isdigit():
        border = int(message.text) #преобразует строку в число
        if border == 0:
            bot.send_message(message.chat.id, 'Брат, пришли мне положительное число')
        else:
            number = random.randint(1, border) #получаем случайное число
            bot.send_message(message.chat.id, number) #отправляем его
    else:
        bot.send_message(message.chat.id, 'Брат, пришли мне положительное число')

bot.polling(non_stop=True)