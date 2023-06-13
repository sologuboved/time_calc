import datetime


def process_timelet(timelet):
    timelet = dict(zip(('seconds', 'minutes', 'hours'), map(int, reversed(timelet.strip().split(':')))))
    for key in ('minutes', 'hours'):
        timelet.setdefault(key, 0)
    return datetime.timedelta(**timelet)


def process_date(date):
    date = date.strip()
    today = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
    if date == 'today':
        return today
    date = dict(zip(('day', 'month', 'year'), map(int, date.split('.'))))
    date.setdefault('month', today.month)
    date.setdefault('year', today.year)
    return datetime.datetime(**date)


if __name__ == '__main__':
    print(process_timelet('03:2:01'))
