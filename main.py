import telebot

bot = telebot.TeleBot('1008393906:AAFwqxLIL_PJmK7wzw1dUTj0Uba_N6qooaU')
vk_link = 'https://vk.me/join/AJQ1d/s5XRYmhdwRybzDtnPK'
whatsapp_link = 'https://chat.whatsapp.com/CSoFfzxo5vd3rWu8NBFdYE'
ya_link = 'ya.ru'
google_link = 'google.ru'


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Спасибо, что я родился, {message.from_user.first_name}')


@bot.message_handler(commands=['links'])
def links_message(message):
    bot.send_message(message.chat.id, f'Ссылки:\nWhatsApp: {whatsapp_link}\nВконтакте: {vk_link}')


@bot.message_handler(commands=['commands'])
def links_message(message):
    bot.send_message(message.chat.id, f'Команды:\n'
                                      f'/links-ссылки на группы\n'
                                      f'/start-родить бота\n'
                                      f'/commands-список команд\n'
                                      f'Сообщения:\n'
                                      f'"вк", "хачю века", "хочу вк" - ссылка на вк группу\n'
                                      f'"ватсап", "хачю ватсап", "хочу ватсап" - ссылка на ватсап группу\n'
                                      f'"гугл" - ссылка на Google\n'
                                      f'"яндекс" - ссылка на Яндекс')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    if message.text.lower() == 'пока':
        bot.send_message(message.chat.id, f'Пока, {message.from_user.first_name}')
    if message.text.lower() in ['хачю века', 'вк', 'хочу вк']:
        bot.send_message(message.chat.id, f'{vk_link}')
    if message.text.lower() in ['хачю ватсап', 'ватсап', 'хочу ватсап']:
        bot.send_message(message.chat.id, f'{whatsapp_link}')
    if message.text.lower() == 'яндекс':
        bot.send_message(message.chat.id, f'{ya_link}')
    if message.text.lower() == 'гугл':
        bot.send_message(message.chat.id, f'{google_link}')
    if message.text.lower() in ['дз', 'шкила', 'дневник']:
        pass
        # bot.send_message(message.chat.id, f'{}')
    if 'карамба' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIbmF4snDLWelBR7EFB2UPAUUmSVeG9AAIIAAPANk8Tb2wmC94am2kYBA')


bot.polling()
