#echo_bot.py
import telebot

#register the telesky bot with it's bot token
bot = telebot.Telebot("1546673599:AAFxDNlWrxMytDK18KH4_2AxJhxIawclfes")

#message handlers for /start and /help
@bot.message_handler(commands=['start", 'help'])
def send_welcome(message):
	bot.reply_to(message, "howdy, how are you doing?")

#echo all messages
@bot.message_handler(func=lambda message: true)
def echo_all(message):
	bot.reply_to(message, message.text)

#start bot
bot.polling()





