import datetime


def process_timelapse(timelet, seconds_first):
    keys = ['hours', 'minutes', 'seconds']
    timelet = timelet.strip().split(':')
    if seconds_first:
        keys.reverse()
        timelet.reverse()
    timelet = dict(zip(keys, map(int, timelet)))
    for key in keys[:-1]:
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


def process_datetimelet(date, timelet):
    return process_date(date) + process_timelapse(timelet, seconds_first=False)


if __name__ == '__main__':
    print(process_datetimelet('13.06.2023', '18:15'))
