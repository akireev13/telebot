import telebot
from tabulate import tabulate

bot = telebot.TeleBot("5904096013:AAHvx7447qJUXYiyvjNU8ZIZ1t6-smGXhCk", parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup()
markup2 = telebot.types.InlineKeyboardMarkup()
markup3 = telebot.types.InlineKeyboardMarkup()
start_game = telebot.types.KeyboardButton('/game')
choose_X = telebot.types.InlineKeyboardButton('X', callback_data='X')
choose_O = telebot.types.InlineKeyboardButton('O', callback_data='O')

btn11 = telebot.types.InlineKeyboardButton(' ', callback_data='btn11')
btn12 = telebot.types.InlineKeyboardButton(' ', callback_data='btn12')
btn13 = telebot.types.InlineKeyboardButton(' ', callback_data='btn13')
btn21 = telebot.types.InlineKeyboardButton(' ', callback_data='btn21')
btn22 = telebot.types.InlineKeyboardButton(' ', callback_data='btn22')
btn23 = telebot.types.InlineKeyboardButton(' ', callback_data='btn23')
btn31 = telebot.types.InlineKeyboardButton(' ', callback_data='btn31')
btn32 = telebot.types.InlineKeyboardButton(' ', callback_data='btn32')
btn33 = telebot.types.InlineKeyboardButton(' ', callback_data='btn33')

markup.add(start_game)
markup2.add(choose_X, choose_O)
markup3.add(btn11, btn12, btn13, btn21, btn22, btn23, btn31, btn32, btn33)

@bot.message_handler(commands=['start'])
def answer(message):
    bot.send_message(message.chat.id, 'let\'s play', reply_markup=markup)

@bot.message_handler(commands=['game'])
def start_message(message):

    bot.send_message(message.chat.id, 'выбери сторону', reply_markup=markup2)
    

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if (req[0] == 'X'):
        player_side = 1
    else:
        player_side = 0

    if player_side == 1:
        bot.send_message(call.message.chat.id, 'ходи', reply_markup=markup3)






bot.infinity_polling()