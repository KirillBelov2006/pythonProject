import telebot

TOKEN = '6894213566:AAHsQ-ksQWvVRQzDdMKizDvSKA3R9Y6RNOs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Приветствую вас {message.chat.username} на боте по конвертации валют')

@bot.message_handler(content_types=['photo'])
def get_comment_to_photo(message):
    bot.reply_to(message,'Nice,meme XDD')




bot.polling(none_stop=True, interval=0)