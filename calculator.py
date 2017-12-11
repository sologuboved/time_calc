import datetime

INCORRECT_INPUT = "Incorrect input!"
DELIMITER = '/'

# TODO input: date, num of days; output: date after num of days elapsed + day of week
# TODO input: date, num of days; output: date  num of days ago + day of week
# TODO input: date1, date2; output: num of days between date1 and date2
# TODO input: time1, time2, time3, ...; output: sum
# TODO reverse dates in input


def process_datelapse(user_input):
    user_input = map(lambda i: i.strip(), user_input.split(DELIMITER))
    try:
        raw_date, raw_lapse = user_input
        return process_date(raw_date), process_lapse(raw_lapse)
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
        raw_date = list(map(int, raw_date.split()))
    except ValueError:
        return

    raw_date.reverse()
    length = len(raw_date)

    if length > 3 or not length:
        return

    if length == 3:
        try:
            return datetime.date(*raw_date)
        except (TypeError, ValueError):
            return

    this_year = datetime.date.today().year

    if length == 1:
        this_month = datetime.date.today().month
        try:
            return datetime.date(this_year, this_month, *raw_date)
        except (TypeError, ValueError):
            return

    try:
        return datetime.date(this_year, *raw_date)
    except (TypeError, ValueError):
        return


def process_lapse(raw_lapse):
    try:
        return datetime.timedelta(int(raw_lapse))
    except ValueError:
        return


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
    date, lapse = process_datelapse(user_input)
    if not (date and lapse):
        return INCORRECT_INPUT
    try:
        return process_ouput(date + lapse, False)
    except OverflowError:
        return INCORRECT_INPUT


def before(user_input):
    date, lapse = process_datelapse(user_input)
    if not (date and lapse):
        return INCORRECT_INPUT
    try:
        return process_ouput(date - lapse, False)
    except OverflowError:
        return INCORRECT_INPUT


def between(user_input):
    start, end = process_datedate(user_input)
    if not (start and end):
        return INCORRECT_INPUT
    try:
        return process_ouput(abs(end - start), True)
    except OverflowError:
        return INCORRECT_INPUT


def add(user_input):
    pass


# >>> d.strftime("%A %d. %B %Y")
# 'Monday 11. March 2002'
# >>> 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
# 'The day is 11, the month is March.'


if __name__ == '__main__':
    pass
    # print(abs(int(str(datetime.date(2016, 11, 12) - datetime.date(2017, 12, 11)).split()[0])))
    # print(datetime.date((2000, 2, 10)))
    # l = [2000, 1, 1]
    # print(datetime.date(*l))
    # s = ''
    # print(not len(s.split()))
    # print(after('a', '2'))
    # print(after("today / 1000000"))
    print(between("today / 1 01"))


