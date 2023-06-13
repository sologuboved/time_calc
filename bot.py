import logging

from telegram.ext import Application, CommandHandler

from calc_ops import process_datedelta, process_datelapse
from helpers import report_exception, write_pid
from output_processor import process_date, process_days
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
        process_date(process_datelapse(get_query(update))),
    )


async def datedelta(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        process_days(process_datedelta(get_query(update))),
    )


async def timelets(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        process_days(process_datedelta(get_query(update))),
    )


def get_query(update):
    return update['message']['text'].split(maxsplit=1)[-1].strip()


@report_exception
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('dateday', datelapse))
    application.add_handler(CommandHandler('datedate', datedelta))
    application.run_polling()


if __name__ == '__main__':
    write_pid()
    main()
