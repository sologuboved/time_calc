import datetime


def process_timelapse(timelapse, zero_seconds):
    keys = ['seconds', 'minutes', 'hours', 'days']
    timelapse = timelapse.strip().split(':')
    if zero_seconds:
        timelapse.append(0)
    timelapse.reverse()
    timelapse = dict(zip(keys, map(int, timelapse)))
    for key in keys[:-1]:
        timelapse.setdefault(key, 0)
    return datetime.timedelta(**timelapse)


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
    if timelet == 'now':
        return datetime.datetime.now()
    return process_date(date) + process_timelapse(timelet, zero_seconds=True)


if __name__ == '__main__':
    print(process_datetimelet('13.06.2023', '18:15'))
