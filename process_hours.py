import datetime
from global_vars import *
from process_days import process_date


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


# def process_time_series(user_input):
#     user_input = user_input.split()
#     length = len(user_input)
#     if not length or length % 2 == 0:
#         return
#
    # first_timelet = process_timelet(user_input[0])
    # if not first_timelet:
    #     return
    # curr_res = convert_to_secs(*first_timelet)
    # if not curr_res:
    #     return
    # ind = 1
    # while ind + 1 < length:
    #     sign = user_input[ind]
    #
    #     if sign == PLUS:
    #         curr_res = add(curr_res, user_input[ind + 1], negative=False)
    #     elif sign == MINUS:
    #         curr_res = add(curr_res, user_input[ind + 1], negative=True)
    #     elif sign == ASTERIX:
    #         curr_res = multiply(curr_res, user_input[ind + 1])
    #     else:
    #         return
    #
    #     if curr_res is None:
    #         return
    #     ind += 2
    # return convert_to_dhms(curr_res)


def process_timelet(raw_timelet):
    if raw_timelet == 'now':
        now = datetime.datetime.now()
        return 0, now.hour, now.minute, now.second

    try:
        raw_timelet = dict(enumerate(reversed(list(map(int, raw_timelet.split(DOT))))))
    except ValueError:
        return

    if len(raw_timelet) > 4:
        return

    return raw_timelet.get(3, 0), raw_timelet.get(2, 0), raw_timelet.get(1, 0), raw_timelet.get(0, 0)


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
        days, hrs, mins, secs = timelet
        if hrs > 23 or mins > 59 or secs > 59:
            timelet = None

    return process_date(raw_date), timelet


def process_time_output(output, delta):
    if delta:
        days, hrs, mins, secs = output
        if days == 1:
            inflection = ''
        else:
            inflection = 's'
        return "%d day%s, %d:%d.%d" % (days, inflection, hrs, mins, secs)


def convert_to_dhms(raw_secs):
    secs = raw_secs % 60
    raw_mins = raw_secs // 60
    mins = raw_mins % 60
    raw_hrs = raw_mins // 60
    hrs = raw_hrs % 24
    days = raw_hrs // 24
    return days, hrs, mins, secs


def convert_to_secs(days, hours, mins, secs):
    return days * 24 * 60 * 60 + hours * 60 * 60 + mins * 60 + secs


def add(secs, raw_timelet, negative):
    timelet = process_timelet(raw_timelet)
    if not timelet:
        return
    if negative:
        return secs - convert_to_secs(*timelet)
    return secs + convert_to_secs(*timelet)


def multiply(secs, integer):
    try:
        integer = int(integer)
    except ValueError:
        return
    return secs * integer


# def convert_timelet(timelet):
#     raw_hrs, raw_mins, raw_secs = timelet
#     secs = raw_secs % 60
#     raw_mins += raw_secs // 60
#     mins = raw_mins % 60
#     raw_hrs += raw_mins // 60
#     hrs = raw_hrs % 24
#     days = raw_hrs // 24
#     return days, hrs, mins, secs


if __name__ == '__main__':
    print(process_time_series("17.12 + 1.10 - 5"))
    print(process_time_series("23.55.55 + 6.6 + 1"))
    print(process_time_series("27.0 * 2"))
    print(process_time_series("1.56.17 - 8.0 - 1.0.0 + 1 + 20.7 - 1.0"))
    print(process_time_series("1.56.17 - 8.0 - 1.0.0 * 2 + 1 + 20.7 - 1.0"))
