import datetime
from global_vars import *


def process_datelapse(user_input):
    user_input = map(lambda i: i.strip(), user_input.split(DELIMITER))
    try:
        raw_date, raw_lapse = user_input
        return process_date(raw_date), process_daylapse(raw_lapse)
    except ValueError:
        return None, None


def process_datedate(user_input):
    user_input = map(lambda i: i.strip(), user_input.split(DELIMITER))
    try:
        start, end = map(lambda i: process_date(i), user_input)
        return start, end
    except ValueError:
        return None, None


def process_date(raw_date):
    if raw_date == 'today':
        return datetime.date.today()

    try:
        date = list(map(int, map(lambda i: i.strip(), raw_date.split(DOT))))
    except ValueError:
        return

    date.reverse()
    length = len(date)

    if not length or length > 3:
        return

    if length == 3:
        try:
            return datetime.date(*date)
        except (TypeError, ValueError):
            return

    this_year = datetime.date.today().year

    if length == 1:
        this_month = datetime.date.today().month
        try:
            return datetime.date(this_year, this_month, *date)
        except (TypeError, ValueError):
            return

    try:
        return datetime.date(this_year, *date)
    except (TypeError, ValueError):
        return


def process_daylapse(raw_lapse):
    try:
        return datetime.timedelta(int(raw_lapse))
    except ValueError:
        return
