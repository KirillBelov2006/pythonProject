import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot("6862483006:AAHgzit9qJ7oUNi9kGa31X0Eby1ZCgC8MLU")


@bot.message_handler(commands=['start'])
def lang(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🇬🇧 English")
    item2 = types.KeyboardButton("🇷🇺 Русский")
    markup.add(item1,item2)
    bot.send_message(message.chat.id, "Choose your language/Выберите свой язык",  reply_markup=markup)

@bot.message_handler(content_types =['text'])
def eng_info(message):
    if message.chat.type == 'private':
        if message.text == "🇬🇧 English":

            bot.send_message(message.chat.id, f' We greet you <b>{message.from_user.first_name} {message.from_user.last_name}</b> on the bot page of the <b>DAT company (Digital Augmented Technologies)</b> . The Menu directory contains the main bot commands',parse_mode='html')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("📁 Company")
            item2 = types.KeyboardButton("💻 EDUCITY METAVERSE")
            item3 = types.KeyboardButton("🤙 Сontact us")
            item4 = types.KeyboardButton("🤝 Сollaboration")
            item5 = types.KeyboardButton("🌐 Social media")
            item6 = types.KeyboardButton("🛠️ Technical assistance")
            item7 = types.KeyboardButton("🔁Return to menu")
            markup.add(item1, item2, item3, item4, item5, item6, item7)
            bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

        if message.text == "🇷🇺 Русский":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("📁 О компании")
            item2 = types.KeyboardButton("💻 EDUCITY")
            item3 = types.KeyboardButton("🤙 Связь с нами")
            item4 = types.KeyboardButton("🤝 Cотрудничество")
            item5 = types.KeyboardButton("🌐 Соц.сети")
            item6 = types.KeyboardButton("🛠️ Тех.Помощь")
            item7 = types.KeyboardButton("🔁Вернуться в меню")

            markup.add(item1, item2, item3, item4, item5, item6, item7)
            bot.send_message(message.chat.id,
                             f'Приветствуем вас <b>{message.from_user.first_name} {message.from_user.last_name}</b> на бот странице компании <b>DAT (Digital Augmented Technologies)</b>\n\nВ каталоге <b>Menu(Меню)</b> указаны основные команды бота ',
                             parse_mode='html', reply_markup=markup)

        elif message.text == '📁 Company':
            bot.send_message(message.chat.id, "We understand that virtual reality technologies are the future. Therefore, we never cease to improve our skills and bring ideas to life.\n\nDuring our work, we have implemented projects such as visualization of a residential complex. We created a helpsult simulator. We create 3D instructions for goods or equipment.\n\nOur platform for learning foreign languages has no direct analogues. We take an innovative approach to solving problems.\n\nThere are projects for creating avatars, locations and a library of 3D models. We discuss the project in detail with the customer, help in solving the problem.\n\n<b>Our achievements:</b>\n\n✅ Winners of a regional grand in the medical field.\n✅⠀We specialize in developments in the fields of education, medicine, construction.\n✅⠀We have been successfully implementing projects since 2021.\n✅ We are residents of the IT Park\n\n<b>Our website:</b>\nhttps://datechnologies.tech/",parse_mode='html')

        elif message.text == '💻 EDUCITY METAVERSE':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Telegram Group")
            item2 = types.KeyboardButton("EDUCITY on WEB")
            item3 = types.KeyboardButton("Introductory video")
            item4 = types.KeyboardButton("⬅️ Back")
            markup.add(item1,item2, item3, item4)
            bot.reply_to(message, 'Выберите действие', reply_markup=markup)

        elif message.text == "Telegram Group":
            bot.send_message(message.chat.id, "https://t.me/Dat_inc")

        elif message.text == "EDUCITY on WEB":
            bot.send_message(message.chat.id, "https://datechnologies.tech/prodj")

        elif message.text == "Introductory video":
            bot.send_message(message.chat.id, ("https://drive.google.com/drive/folders/1VFQut_BziBKnJ49kDSL2s9yDKOzkI3ZY?direction=a") )


        elif message.text == "⬅️ Back":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("📁 Company")
            item2 = types.KeyboardButton("💻 EDUCITY METAVERSE")
            item3 = types.KeyboardButton("🤙 Сontact us")
            item4 = types.KeyboardButton("🤝 Сollaboration")
            item5 = types.KeyboardButton("🌐 Social media")
            item6 = types.KeyboardButton("🛠️ Technical assistance")
            item7 = types.KeyboardButton("🔁Return to menu")

            markup.add(item1, item2, item3, item4, item5, item6, item7)
            bot.send_message(message.chat.id, "Choose an option:", parse_mode='html', reply_markup=markup)
            

        elif message.text == "🤙 Сontact us":
            bot.send_message(message.chat.id,'Email: da@technologies65.ru\nPhone: +7 (914) 087-54-84 \nPhone: +7 (914) 759-74-56' )

        elif message.text == "🤝 Сollaboration":
            bot.send_message(message.chat.id, 'For questions regarding cooperation, please contact https://t.me/dima_garnov')


        elif message.text == "🌐 Social media":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Instagram")
            item2 = types.KeyboardButton("Telegram")
            item3 = types.KeyboardButton("VK")
            item4 = types.KeyboardButton("WhatsApp")
            back = types.KeyboardButton("⬅️ Bаck")
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Choose social media', reply_markup=markup)

        elif message.text == "Instagram":
            bot.send_message(message.chat.id, ("https://www.instagram.com/"))

        elif message.text == "Telegram":
            bot.send_message(message.chat.id, "https://t.me/Dat_inc")

        elif message.text == "🛠️ Technical assistance":
            bot.send_message(message.chat.id, "For help, contact https://t.me/Kirill_DAT")


        elif message.text == "⬅️ Bаck":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("📁 Company")
            item2 = types.KeyboardButton("💻 EDUCITY METAVERSE")
            item3 = types.KeyboardButton("🤙 Сontact us")
            item4 = types.KeyboardButton("🤝 Сollaboration")
            item5 = types.KeyboardButton("🌐 Social media")
            item6 = types.KeyboardButton("🛠️ Technical assistance")
            item7 = types.KeyboardButton("🔁Return to menu")

            markup.add(item1, item2, item3, item4, item5, item6, item7)
            bot.send_message(message.chat.id, "Choose an option:", parse_mode='html', reply_markup=markup)


        elif message.text == "🔁Return to menu":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🇬🇧 English")
            item2 = types.KeyboardButton("🇷🇺 Русский")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Choose your language/Выберите свой язык", reply_markup=markup)







        elif message.text == '📁 О компании':
            bot.send_message(message.chat.id,"Мы понимаем, что за технологиями виртуальной реальности будущее. Поэтому мы не перестаём совершенствовать свои навыки и воплощаем идеи в жизнь.\n\nЗа время работы мы реализовали такие проекты, как визуализация жилого комплекса. Создали тренажёр помогсульта. Создаем 3D инструкции для товаров или оборудования.\n\nНаша платформа по изучению иностранных языков не имеет прямых аналогов. Инновационно подходим к решению задач.\n\nЕсть проекты по созданию аватаров, локаций и библиотека 3D моделей. С заказчиком подробно обсуждаем проект, помогаем в решении проблемы.\n\n<b>Наши достижения:</b>\n\n✅   Победители регионального гранда в медицинской сфере.\n✅⠀Специализируемся на разработках в областях образования, медицины, строительства.\n✅⠀Успешно реализуем проекты с 2021 года.\n✅   Являемся резидентами ИТ Парка\n\n<b>Наш веб сайт:</b>\nhttps://datechnologies.tech/",parse_mode='html')

        elif message.text == "💻 EDUCITY":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Телеграм")
            item2 = types.KeyboardButton("Веб страница EDUCITY ")
            item3 = types.KeyboardButton("Ознакомительное видео")
            item4 = types.KeyboardButton("⬅️ Назад")
            markup.add(item1, item2, item3, item4)
            bot.reply_to(message, 'Выберите действие', reply_markup=markup)

        elif message.text == "Телеграм":
            bot.send_message(message.chat.id, "https://t.me/Dat_inc")
        elif message.text == "Веб страница EDUCITY":
            bot.send_message(message.chat.id, "https://datechnologies.tech/prodj")
        elif message.text == "Ознакомительное видео":
            bot.send_message(message.chat.id,
                             ("https://drive.google.com/drive/folders/1VFQut_BziBKnJ49kDSL2s9yDKOzkI3ZY?direction=a"))



        elif message.text == '🤙 Связь с нами':
            bot.send_message(message.chat.id,
                                     'Email: da@technologies65.ru\nТелефон: +7 (914) 087-54-84 \nТелефон: +7 (914) 759-74-56')

        elif message.text == '🤝 Cотрудничество':
            bot.send_message(message.chat.id,
                                     'По вопросам сотрудничества обращаться к https://t.me/dima_garnov')

        if message.text == '🌐 Соц.сети':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Instаgram")
            item2 = types.KeyboardButton("Tеlegram")
            item3 = types.KeyboardButton("VK")
            item4 = types.KeyboardButton("WhatsApp")
            back = types.KeyboardButton("⬅️ Назад")
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Выберите Соц.сеть', reply_markup=markup)
        elif message.text == "Instаgram":
            bot.send_message(message.chat.id, ("https://www.instagram.com/"))

        elif message.text == "Tеlegram":
            bot.send_message(message.chat.id, "https://t.me/Dat_inc")

        elif message.text == '💡 Тех.Помощь':
            bot.send_message(message.chat.id, 'За помощью обращаться к https://t.me/Kirill_DAT')

        elif message.text == "🛠️ Тех.Помощь":
            bot.send_message(message.chat.id, "За помощью обращаться к https://t.me/Kirill_DAT")

        if message.text == "⬅️ Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("📁 О компании")
            item2 = types.KeyboardButton("💻 EDUCITY")
            item3 = types.KeyboardButton("🤙 Связь с нами")
            item4 = types.KeyboardButton("🤝 Cотрудничество")
            item5 = types.KeyboardButton("🌐 Соц.сети")
            item6 = types.KeyboardButton("🛠️ Тех.Помощь")
            item7 = types.KeyboardButton("🔁Вернуться в меню")
            markup.add(item1, item2, item3, item4, item5, item6, item7 )
            bot.send_message(message.chat.id, "Выберите интересующий вас пункт", parse_mode='html', reply_markup=markup)

        elif message.text == "🔁Вернуться в меню":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🇬🇧 English")
            item2 = types.KeyboardButton("🇷🇺 Русский")
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Choose your language/Выберите свой язык", reply_markup=markup)

@bot.message_handler(content_types=['photo', 'audio', 'document', 'video',])
def get_this_par(message):
    bot.reply_to(message,
                         'Ошибка',
                         parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🇬🇧 English")
    item2 = types.KeyboardButton("🇷🇺 Русский")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Choose your language/Выберите свой язык", reply_markup=markup)


bot.polling(none_stop=True, interval=0)