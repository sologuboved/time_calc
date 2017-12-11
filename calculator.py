import datetime
import time

INCORRECT_INPUT = "Incorrect input!"
DELIMITER = '/'

"""
raw date:
'today'
'11 12 2017' [11 December 2017]
'11 12' [11 December same year as today]
'11' [11 same month and year as today]

raw lapse:
'10' [10 days]

raw timelet:
'now'
'21 11 12' [21:11:12]
'11 12' [00:11:12]
'12' [00:00:12]
"""

# TODO input: lapse1, lapse2, lapse3, ...; output: sum
# TODO input: date time, lapse; output: time after lapse
# TODO input: date time, lapse; output: time before lapse


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


def process_time_series(user_input):
    user_input = user_input.split()


def process_date(raw_date):
    if raw_date == 'today':
        return datetime.date.today()

    try:
        date = list(map(int, raw_date.split()))
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


def process_timelet(raw_timelet):
    if raw_timelet == 'now':
        now = time.localtime()
        return 0, now.tm_hour, now.tm_min, now.tm_sec

    try:
        raw_timelet = list(map(int, raw_timelet.split()))
    except ValueError:
        return

    if len(raw_timelet) > 3:
        return

    raw_timelet = dict(enumerate(reversed(raw_timelet)))
    timelet = (raw_timelet.get(2, 0), raw_timelet.get(1, 0), raw_timelet.get(0, 0))
    return convert_timelet(timelet)


def convert_timelet(timelet):
    raw_hrs, raw_mins, raw_secs = timelet
    secs = raw_secs % 60
    raw_mins += raw_secs // 60
    mins = raw_mins % 60
    raw_hrs += raw_mins // 60
    hrs = raw_hrs % 24
    days = raw_hrs // 24
    return days, hrs, mins, secs


def process_ouput(output, delta):
    if delta:
        output = output.days
        if output == 1:
            inflection = ''
        else:
            inflection = 's'
        return "%d day%s" % (output, inflection)

    return output.strftime("%d %B %Y, %A")


def after(user_input):
    # raw date DELIMITER raw lapse
    date, lapse = process_datelapse(user_input)
    if not (date and lapse):
        return INCORRECT_INPUT
    try:
        return process_ouput(date + lapse, False)
    except OverflowError:
        return INCORRECT_INPUT


def before(user_input):
    # raw date DELIMITER raw lapse
    date, lapse = process_datelapse(user_input)
    if not (date and lapse):
        return INCORRECT_INPUT
    try:
        return process_ouput(date - lapse, False)
    except OverflowError:
        return INCORRECT_INPUT


def between(user_input):
    # raw date DELIMITER raw date
    start, end = process_datedate(user_input)
    if not (start and end):
        return INCORRECT_INPUT
    try:
        return process_ouput(abs(end - start), True)
    except OverflowError:
        return INCORRECT_INPUT


def add(user_input):
    pass


if __name__ == '__main__':
    pass
    print(process_time('302710'))



