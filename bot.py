import logging

from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler

from calc_ops import (
    process_datedelta,
    process_datelapse,
    process_datetimedelta,
    process_datetimelapse,
    process_dow,
    process_howmany,
    process_timelapses,
)
from helpers import report_exception, write_pid
from output_processor import output_date, output_datetimelet, output_days, output_dow, output_num, output_timelet
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


async def info(update, context):
    text = '''
<b>Commands</b>
/datelapse
/datedelta
/timelapses
/howmany
/datetimelapse
/datetimedelta
/dow

<b>Date</b>
<code>today</code>
<code>11.12.2017</code> [11 December 2017]
<code>11.12</code> [11 December same year as today]
<code>11</code> [11 same month and year as today]

<b>Datetimelet's Time Part</b>
<code>4</code> [4 hours]
<code>3:04</code> [3 hours 4 minutes]
<code>2:03:04</code> [2 hours 3 minutes 4 seconds]

<b>Days</b>
<code>4</code> [4 days]

<b>DoW</b>
<code>Mon</code> <code>Tue</code> <code>Wed</code> <code>Thu</code> <code>Fri</code> <code>Sat</code> <code>Sun</code>

<b>Timelet</b>
<code>4</code> [4 seconds]
<code>3:04</code> [3 minutes 4 seconds]
<code>2:03:04</code> [2 hours 3 minutes 4 seconds]
<code>1:02:03:04</code> [1 day 2 hours 3 minutes 4 seconds]
'''
    await context.bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)


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
        output_datetimelet(process_datetimedelta(get_query(update)), include_date=True),
    )


async def dow(update, context):
    await context.bot.send_message(
        update.message.chat_id,
        output_dow(process_dow(get_query(update))),
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
    application.add_handler(CommandHandler('dow', dow))
    application.run_polling()


if __name__ == '__main__':
    write_pid()
    main()
