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
        return datetime.datetime.now(tz=MOSCOW)

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
            return datetime.datetime(*date, tzinfo=MOSCOW)
        except (TypeError, ValueError):
            return

    this_year = datetime.datetime.now().year

    if length == 1:
        this_month = datetime.datetime.now().month
        try:
            return datetime.datetime(this_year, this_month, *date, tzinfo=MOSCOW)
        except (TypeError, ValueError):
            return

    try:
        return datetime.datetime(this_year, *date, tzinfo=MOSCOW)
    except (TypeError, ValueError):
        return


def process_daylapse(raw_lapse):
    try:
        return datetime.timedelta(int(raw_lapse))
    except ValueError:
        return


def process_datedateday(user_input):
    wrong = (None, None, None)
    splitted = list(map(lambda d: d.strip(), user_input.split(DELIMITER)))
    if len(splitted) == 3:
        start, end, week_day = splitted
        start, end = map(lambda d: process_date(d), (start, end))
        week_day = process_day(week_day)
    elif len(splitted) == 2:
        start = process_date('today')
        end, week_day = splitted
        end = process_date(end)
        week_day = process_day(week_day)
    else:
        return wrong
    return start, end, week_day


def process_day(day):
    if day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
        return day
