import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_message =  'Здравствуйте!\nВыберете способ конвертации.'

    #Creating buttons
    markup = types.InlineKeyboardMarkup()
    button_card = types.InlineKeyboardButton(text = 'Card', callback_data = 'Card')
    button_cash = types.InlineKeyboardButton(text = 'Cash', callback_data = 'Cash')
    markup.add(button_card, button_cash)

    bot.send_message(message.chat.id, first_message, reply_markup = markup)

#Refactoring
@bot.message_handler(content_types=['Card'])
def Card_API(message):
    get_message_bot = message.Card.strip()
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text = 'See it')
    markup.add(button)

    bot.send_message(message.chat.id, 'information', reply_markup = markup)

# Запуск бота
bot.polling(none_stop=True)
