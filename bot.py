import logging

from telegram.ext import Application, CommandHandler

from calc_ops import process_datedelta, process_datelapse, process_timelets
from helpers import report_exception, write_pid
from output_processor import output_date, output_days, output_timelet
from userinfo import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING,
)


async def start(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        "Date and Time Calculator\nAdds/subtracts/multiplies hours, calculates dates",
    )


async def datelapse(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        output_date(process_datelapse(get_query(update))),
    )


async def datedelta(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        output_days(process_datedelta(get_query(update))),
    )


async def timelets(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        output_timelet(process_timelets(get_query(update))),
    )


def get_query(update):
    return update['message']['text'].split(maxsplit=1)[-1].strip()


@report_exception
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('datelapse', datelapse))
    application.add_handler(CommandHandler('datedelta', datedelta))
    application.add_handler(CommandHandler('timelets', timelets))
    application.run_polling()


if __name__ == '__main__':
    write_pid()
    main()
