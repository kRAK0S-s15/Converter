import telebot
from telebot import types
import config
import api

bot = telebot.TeleBot(config.TOKEN)

# Start commands buttons
@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_message =  'Hello!\n' + 'Choose a country.'

    # Create buttons
    keyboard = types.InlineKeyboardMarkup()
    button_poland = types.InlineKeyboardButton(text = 'Poland', callback_data = 'button_poland')
    button_belarus = types.InlineKeyboardButton(text = 'Belarus', callback_data = 'button_belarus')
    keyboard.add(button_poland, button_belarus)

    bot.send_message(message.chat.id, first_message, reply_markup = keyboard)

# Add next buttons 
@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    if call.message:
        
        if call.data == 'button_poland':
            keyboard = types.InlineKeyboardMarkup()

            button_national_polish_bank = types.InlineKeyboardButton(text = 'National bank', callback_data = 'button_national_polish_bank')
            keyboard.add(button_national_polish_bank)

            bot.send_message(call.message.chat.id,'Choose a bank', parse_mode='html', reply_markup = keyboard)

        elif call.data == 'button_national_polish_bank':
            keyboard = types.InlineKeyboardMarkup()

            button_national_polish_bank_usd = types.InlineKeyboardButton(text = 'USD', callback_data = 'pol_nat_usd')
            button_national_polish_bank_eur = types.InlineKeyboardButton(text = 'EUR', callback_data = 'pol_nat_eur')
            button_national_polish_bank_byn = types.InlineKeyboardButton(text = 'BYN', callback_data = 'pol_nat_byn')
            keyboard.add(button_national_polish_bank_usd, button_national_polish_bank_eur, button_national_polish_bank_byn)

            bot.send_message(call.message.chat.id, 'NATIONAL <b>POLISH</b> BANK\n' + 'Choose a currency', parse_mode = 'html', reply_markup = keyboard)

        elif call.data == 'pol_nat_usd':
            bot.send_message(call.message.chat.id, f"Course 1 {api.get_pol_currency_last('usd')[0]}")


        elif call.data == 'pol_nat_eur':
            bot.send_message(call.message.chat.id, f"Course 1 {api.get_pol_currency_last('eur')[0]}")

        elif call.data == 'pol_nat_byn':
            bot.send_message(call.message.chat.id, f"Course 10 BYN for the last avaible date: {round(float(100 / api.get_bel_currecy_last('PLN')[1]), 4)} PLN")


        elif call.data == 'button_belarus':
            keyboard = types.InlineKeyboardMarkup()

            button_national_belarusian_bank = types.InlineKeyboardButton(text = 'National bank', callback_data = 'button_national_belarusian_bank')
            keyboard.add(button_national_belarusian_bank)

            bot.send_message(call.message.chat.id, "Choose a bank", parse_mode='html', reply_markup = keyboard)

        elif call.data == 'button_national_belarusian_bank':
            keyboard = types.InlineKeyboardMarkup()

            button_national_belarusian_bank_usd = types.InlineKeyboardButton(text = 'USD', callback_data = 'bel_nat_usd')
            button_national_belarusian_bank_eur = types.InlineKeyboardButton(text = 'EUR', callback_data = 'bel_nat_eur')
            button_national_belarusian_bank_pln = types.InlineKeyboardButton(text = 'PLN', callback_data = 'bel_nat_pln')
            keyboard.add(button_national_belarusian_bank_usd, button_national_belarusian_bank_eur, button_national_belarusian_bank_pln)

            bot.send_message(call.message.chat.id, 'NATIONAL <b>BELARUSSIAN</b> BANK\n' + 'Choose a currency', parse_mode = 'html', reply_markup = keyboard)


        elif call.data == 'bel_nat_usd':
            bot.send_message(call.message.chat.id, f"Course 1 {api.get_bel_currecy_last('USD')[0]}")


        elif call.data == 'bel_nat_eur':
            bot.send_message(call.message.chat.id, f"Course 1 {api.get_bel_currecy_last('EUR')[0]}")


        elif call.data == 'bel_nat_pln':
            bot.send_message(call.message.chat.id, f"Course 10 {api.get_bel_currecy_last('PLN')[0]}")


# Starting the bot
bot.polling(none_stop=True)