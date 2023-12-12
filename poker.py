import telebot

bot = telebot.TeleBot("5904096013:AAHvx7447qJUXYiyvjNU8ZIZ1t6-smGXhCk", parse_mode=None)

@bot.message_handler(commands=['start'])
def answer(message):
    bot.send_message(message.chat.id, 'ky')



bot.infinity_polling()