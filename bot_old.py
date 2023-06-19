from telegram.ext import Updater, CommandHandler
from userinfo import TOKEN
from calculate_days import *
from calculate_hours import *
from pid_operations import write_pid


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


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    help_handler = CommandHandler('help', description)
    dow_handler = CommandHandler('dow', dow)

    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(dow_handler)

    updater.start_polling()


if __name__ == '__main__':
    write_pid()
    main()
