import asyncio
from functools import wraps
import logging
import os
import re
import sys
import traceback

from telegram import Bot

from userinfo import TELETRACEBACKS_CHAT_ID, TOKEN


def report_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            notification = f"({func.__name__}, called with {args}, {kwargs}) {type(e).__name__}: {e}"
            asyncio.run(Bot(token=TOKEN).send_message(
                chat_id=TELETRACEBACKS_CHAT_ID,
                text=notification,
                disable_web_page_preview=True,
            ))
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
