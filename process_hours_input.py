import datetime
from global_vars import *
from process_days_input import process_date


def process_time_series(user_input):
    user_input = user_input.split()
    length = len(user_input)
    if not length or length % 2 == 0:
        return

    processed_series = list()
    even = True
    after_asterix = False
    for item in user_input:
        if even:
            if after_asterix:
                try:
                    item = int(item)
                except ValueError:
                    return
                after_asterix = False
            else:
                item = process_timelet(item)
            if not item:
                return
            processed_series.append(item)
        else:
            if item == ASTERIX:
                after_asterix = True
            elif item != PLUS and item != MINUS:
                return
            processed_series.append(item)
        even = not even
    return processed_series


def process_timelet(raw_timelet):
    if raw_timelet == 'now':
        now = datetime.datetime.now()
        return now.hour, now.minute, now.second

    try:
        raw_timelet = dict(enumerate(reversed(list(map(int, raw_timelet.split(DOT))))))
    except ValueError:
        return

    if len(raw_timelet) > 3:
        return

    return raw_timelet.get(2, 0), raw_timelet.get(1, 0), raw_timelet.get(0, 0)


def process_timelapse(user_input):
    user_input = map(lambda i: i.strip(), user_input.split(DELIMITER))

    try:
        raw_datetime, raw_lapse = user_input
    except ValueError:
        return None, None, None

    date, timelet = process_datetime(raw_datetime)
    return date, timelet, process_timelet(raw_lapse)


def process_timetime(user_input):
    user_input = map(lambda i: i.strip(), user_input.split(DELIMITER))

    try:
        start, end = user_input
    except ValueError:
        return None, None, None, None

    start_date, start_time = process_datetime(start)
    end_date, end_time = process_datetime(end)
    return start_date, start_time, end_date, end_time


def process_datetime(raw_datetime):
    raw_datetime = raw_datetime.split()

    try:
        raw_date, raw_time = raw_datetime

    except ValueError:
        if len(raw_datetime) == 1:
            raw_date = 'today'
            raw_time = raw_datetime[0]
        else:
            return None, None

    timelet = process_timelet(raw_time)
    if timelet:
        hrs, mins, secs = timelet
        if hrs > 23 or mins > 59 or secs > 59:
            timelet = None

    return process_date(raw_date), timelet


def convert_to_dhms(raw_secs):
    if raw_secs < 0:
        raw_secs = abs(raw_secs)
        mult_by = -1
    else:
        mult_by = 1
    secs = raw_secs % 60
    raw_mins = raw_secs // 60
    mins = raw_mins % 60
    hrs = raw_mins // 60
    return tuple(map(lambda u: u * mult_by, [hrs, mins, secs]))


def convert_to_secs(*units):
    for unit in units:
        if unit < 0:
            mult_by = -1
            units = map(abs, units)
            break
    else:
        mult_by = 1

    hours, mins, secs = units

    return mult_by * (hours * 60 * 60 + mins * 60 + secs)


if __name__ == '__main__':
    print(process_time_series("17.12 + 1.10 - 5"))
    print(process_time_series("23.55.55 + 6.6 + 1"))
    print(process_time_series("27.0 * 2"))
    print(process_time_series("1.56.17 - 8.0 - 1.0.0 + 1 + 20.7 - 1.0"))
    print(process_time_series("1.56.17 - 8.0 - 1.0.0 * 2 + 1 + 20.7 - 1.0"))
