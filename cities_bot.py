import telebot
import random

bot = telebot.TeleBot('TOKEN_HERE')

file = open('cities.txt', encoding='UTF-8')
cities = file.readlines()
for i in range(len(cities)):
    cities[i] = cities[i].strip() #убираем лишние символы

@bot.message_handler(commands=['start'])
def start_message_response(message):
    bot.send_message(message.chat.id, 'Привет, давай сыграем с тобой в города, я начну')
    number = random.randint(0, len(cities) - 1)
    bot.send_message(message.chat.id, cities[number])

@bot.message_handler(content_types=['text'])
def any_message_response(message):
    length = len(message.text)
    last_letter = message.text[length - 1].upper()
    current_list = [city for city in cities if city.startswith(last_letter)] #получим все города на эту букву
    city = random.choice(current_list)
    bot.send_message(message.chat.id, city)

bot.polling(non_stop=True)