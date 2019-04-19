from telegram.ext import Updater, CommandHandler
from tkn import TOKEN
from calculate_days import *
from calculate_hours import *
from pid_operations import write_pid


def start(bot, update):
    text = "Date and Time Calculator\n" \
           "Adds/subtracts/multiplies hours, calculates dates"
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)


def description(bot, update):
    text = "Commands: \n\n" \
           "/daft - date %s lapse\n" \
           "/dbef - date %s lapse\n" \
           "/dbetw - date %s date\n" \
           "/dow - date\n" \
           "/howm - date %s date %s day of week or date %s day of week\n\n" \
           "/taft - date timelet %s timelet\n" \
           "/tbef - date timelet %s timelet\n" \
           "/tbetw - date timelet %s date timelet\n" \
           "/tseq - timelet {+, -, *} timelet {+, -, *} ... \n\n\n" \
           "date:\n\n" \
           "'today'\n" \
           "'11.12.2017' [11 December 2017]\n" \
           "'11.12' [11 December same year as today]\n" \
           "'11' [11 same month and year as today]\n\n" \
           "lapse:\n\n" \
           "'10' [10 days]\n\n" \
           "day of week:\n\n{Mon, Tue, Wed, Thu, Fri, Sat, Sun}\n\n" \
           "timelet:\n\n" \
           "'now'\n" \
           "'21:11:12'\n" \
           "'11:12' [00:11:12]\n" \
           "'12' [00:00:12]\n" % (
               DELIMITER, DELIMITER, DELIMITER, DELIMITER, DELIMITER, DELIMITER, DELIMITER, DELIMITER, DELIMITER)

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=text)


def daft(bot, update):
    # /daft today / 10
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = date_after(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def dbef(bot, update):
    # /dbef 11 / 10
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = date_before(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def dbetw(bot, update):
    # /dbetw 13.12 / 1.3.2018
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = days_between(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def dow(bot, update):
    # /dow "15.12.2017"
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = get_day_of_week(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def howm(bot, update):
    # /howm "2.1.2018 / 1.3.2018 / Thu"
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = how_many(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def taft(bot, update):
    # /taft 13.12.2017 23:56:52 / 3:8
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = time_after(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def tbef(bot, update):
    # /tbef 14.12.2017 0:10:0 / 48:11:0
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = time_before(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def tbetw(bot, update):
    # /tbetw 13.12.2017 12:28:0 / 12.12.2017 0:59:0
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = time_between(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def tseq(bot, update):
    # /tseq 1:56:17 - 8:0 - 1:0:0 + 0 + 20:7 - 1:0
    query = update['message']['text']
    print('query:', query)
    query = query.split()
    try:
        query = ' '.join(query[1:])
    except IndexError:
        query = ''
    reply = calculate_time_sequence(query)
    print('reply:', reply, '\n')
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def today(bot, update):
    # /today
    reply = get_today()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def now(bot, update):
    # /now
    reply = get_now()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=reply)


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', description)
    daft_handler = CommandHandler('daft', daft)
    dbef_handler = CommandHandler('dbef', dbef)
    dbetw_handler = CommandHandler('dbetw', dbetw)
    taft_handler = CommandHandler('taft', taft)
    tbef_handler = CommandHandler('tbef', tbef)
    tbetw_handler = CommandHandler('tbetw', tbetw)
    tseq_handler = CommandHandler('tseq', tseq)
    dow_handler = CommandHandler('dow', dow)
    howm_handler = CommandHandler('howm', howm)
    now_handler = CommandHandler('now', now)
    today_handler = CommandHandler('today', today)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(daft_handler)
    dispatcher.add_handler(dbef_handler)
    dispatcher.add_handler(dbetw_handler)
    dispatcher.add_handler(taft_handler)
    dispatcher.add_handler(tbef_handler)
    dispatcher.add_handler(tbetw_handler)
    dispatcher.add_handler(tseq_handler)
    dispatcher.add_handler(dow_handler)
    dispatcher.add_handler(howm_handler)
    dispatcher.add_handler(now_handler)
    dispatcher.add_handler(today_handler)

    updater.start_polling()


if __name__ == '__main__':
    write_pid()
    main()
