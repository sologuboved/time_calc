from functools import wraps
import logging
import os
import re
import sys
import traceback


def report_wrong_input(func):
    @wraps(func)
    async def wrapper(update, context):
        try:
            await func(update, context)
        except ValueError:
            await context.bot.send_message(
                chat_id=update.message.chat_id,
                text=f"Wrong input: Not enough data",
            )
            traceback_msg = traceback.format_exc()
            logging.error(traceback_msg)
    return wrapper


def get_base_dir():
    return os.path.dirname(os.path.abspath(__file__))


def get_abs_path(fname):
    return os.path.join(get_base_dir(), fname)


def write_pid():
    prefix = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    previous_pid = find_previous_pid(prefix)
    if previous_pid:
        print("\nRemoving {}...".format(previous_pid))
        os.remove(previous_pid)
    pid_fname = get_abs_path('{}_{}.pid'.format(prefix, str(os.getpid())))
    print("Writing {}\n".format(pid_fname))
    with open(pid_fname, 'w') as handler:
        handler.write(str())
    return pid_fname


def delete_pid(pid_fname):
    try:
        os.remove(pid_fname)
    except FileNotFoundError as e:
        print(str(e))


def find_previous_pid(prefix):
    for fname in os.listdir(get_base_dir()):
        if re.fullmatch(r'{}_\d+\.pid'.format(prefix), fname):
            return get_abs_path(fname)
