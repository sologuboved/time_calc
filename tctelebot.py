from telegram.ext import Updater, CommandHandler
from tkn import TOKEN
from calculate_days import *
from calculate_hours import *


def start(bot, update):
    text = "Date and Time Calculator\n" \
           "Adds/subtracts/multiplies hours, calculates dates"
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)


def daft(bot, update):
    # /daft today / 10
    try:
        query = update['message']['text']
        query = query.split()
        query = ' '.join(query[1:])
        print(query)
    except IndexError:
        query = ''
    reply = date_after(query)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def dbef(bot, update):
    # /dbef 11 / 10
    try:
        query = update['message']['text']
        query = query.split()
        query = ' '.join(query[1:])
        print(query)
    except IndexError:
        query = ''
    reply = date_before(query)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def dbetw(bot, update):
    # /dbetw 13.12 / 1. 3. 2018
    try:
        query = update['message']['text']
        query = query.split()
        query = ' '.join(query[1:])
        print(query)
    except IndexError:
        query = ''
    reply = days_between(query)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)
    
    
def taft(bot, update):
    # /taft 13.12.2017 23.56.52 / 3.8
    try:
        query = update['message']['text']
        query = query.split()
        query = ' '.join(query[1:])
        print(query)
    except IndexError:
        query = ''
    reply = time_after(query)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)
    
    
def tbef(bot, update):
    # /tbef 14.12.2017 0.10.0 / 48.11.0
    try:
        query = update['message']['text']
        query = query.split()
        query = ' '.join(query[1:])
        print(query)
    except IndexError:
        query = ''
    reply = time_before(query)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)
    
    
def tbetw(bot, update):
    # /tbetw 13.12.2017 12.28.0 / 12.12.2017 0.59.0
    try:
        query = update['message']['text']
        query = query.split()
        query = ' '.join(query[1:])
        print(query)
    except IndexError:
        query = ''
    reply = time_between(query)
    print(reply)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)
    
    
def tseq(bot, update):
    # /tseq 1.56.17 - 8.0 - 1.0.0 + 0 + 20.7 - 1.0
    try:
        query = update['message']['text']
        query = query.split()
        query = ' '.join(query[1:])
        print(query)
    except IndexError:
        query = ''
    reply = calculate_time_sequence(query)
    print(reply)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    daft_handler = CommandHandler('daft', daft)
    dbef_handler = CommandHandler('dbef', dbef)
    dbetw_handler = CommandHandler('dbetw', dbetw)
    taft_handler = CommandHandler('taft', taft)
    tbef_handler = CommandHandler('tbef', tbef)
    tbetw_handler = CommandHandler('tbetw', tbetw)
    tseq_handler = CommandHandler('tseq', tseq)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(daft_handler)
    dispatcher.add_handler(dbef_handler)
    dispatcher.add_handler(dbetw_handler)
    dispatcher.add_handler(taft_handler)
    dispatcher.add_handler(tbef_handler)
    dispatcher.add_handler(tbetw_handler)
    dispatcher.add_handler(tseq_handler)

    updater.start_polling()
