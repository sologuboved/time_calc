import logging

from telegram.ext import Application, CommandHandler

from calc_ops import (
    process_datedelta,
    process_datelapse,
    process_datetimedelta,
    process_datetimelapse,
    process_howmany,
    process_timelapses,
)
from helpers import report_exception, write_pid
from output_processor import output_date, output_datetimelet, output_days, output_num, output_timelet
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


async def timelapses(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        output_timelet(process_timelapses(get_query(update))),
    )


async def howmany(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        output_num(process_howmany(get_query(update))),
    )


async def datetimelapse(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        output_datetimelet(*process_datetimelapse(get_query(update))),
    )


async def datetimedelta(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        output_datetimelet(process_datetimedelta(get_query(update)), True),
    )


def get_query(update):
    return update['message']['text'].split(maxsplit=1)[-1].strip()


@report_exception
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('datelapse', datelapse))
    application.add_handler(CommandHandler('datedelta', datedelta))
    application.add_handler(CommandHandler('timelapses', timelapses))
    application.add_handler(CommandHandler('howmany', howmany))
    application.add_handler(CommandHandler('datetimelapse', datetimelapse))
    application.add_handler(CommandHandler('datetimedelta', datetimedelta))
    application.run_polling()


if __name__ == '__main__':
    write_pid()
    main()
