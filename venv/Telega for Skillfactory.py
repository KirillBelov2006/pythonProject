import telebot
from config import TOKEN, keys
from extensions import Convertor, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Привет! Доступные команды:\n"\
        "/help - Помощь\n"\
        "/values - Увидеть список доступных валют\n"\
        "Введите <конвертируемая валюта> <валюта, в которую конвертируем> <кол-во валюты>"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    values = list(map(str.capitalize, values))
    try:
        result = Convertor.get_price(values)
    except APIException as e:
        bot.reply_to(message, e)
    else:
        text = f'{values[2]} {values[0]} = {result} {values[1]}'
        bot.reply_to(message, text)

bot.polling(none_stop=True, interval=0)