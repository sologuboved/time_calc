import datetime

INCORRECT_INPUT = "Incorrect input!"

# TODO input: date, num of days; output: date after num of days elapsed + day of week
# TODO input: date, num of days; output: date  num of days ago + day of week
# TODO input: date1, date2; output: num of days between date1 and date2
# TODO input: time1, time2, time3, ...; output: sum


def process_date(raw_date):
    if raw_date == 'today':
        return datetime.date.today()

    try:
        raw_date = tuple(map(int, raw_date.split()))
    except ValueError:
        return INCORRECT_INPUT

    print(raw_date)
    length = len(raw_date)
    print(length)
    print()

    if length > 3 or not length:
        return INCORRECT_INPUT

    if length == 3:
        try:
            return datetime.date(*raw_date)
        except (TypeError, ValueError):
            return INCORRECT_INPUT

    this_year = datetime.date.today().year

    if length == 1:
        this_month = datetime.date.today().month
        try:
            return datetime.date(this_year, this_month, *raw_date)
        except (TypeError, ValueError):
            return INCORRECT_INPUT

    try:
        return datetime.date(this_year, *raw_date)
    except (TypeError, ValueError):
        return INCORRECT_INPUT


def after(raw_date, lapse):
    pass


def before():
    pass


def between():
    pass


def add():
    pass


if __name__ == '__main__':
    pass
    # print(abs(int(str(datetime.date(2016, 11, 12) - datetime.date(2017, 12, 11)).split()[0])))
    # print(datetime.date((2000, 2, 10)))
    # l = [2000, 1, 1]
    # print(datetime.date(*l))
    # s = ''
    # print(not len(s.split()))
    print(process_date('15'))


