import datetime
from global_vars import *


def process_time_series(user_input):
    user_input = tuple(map(lambda i: i.strip(), user_input.split()))
    print(user_input)
    length = len(user_input)
    if not length or length % 2 == 0:
        return

    curr_res = user_input[0]
    ind = 1
    while ind < length:
        pass


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
    # print(convert_to_secs(3, 0, 5, 0))
    print(process_timelet('now'))
