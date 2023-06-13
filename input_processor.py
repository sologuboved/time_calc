import datetime


def process_date(date):
    today = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())
    if date == 'today':
        return today
    date = dict(zip(('day', 'month', 'year'), map(int, date.split('.'))))
    date.setdefault('month', today.month)
    date.setdefault('year', today.year)
    return datetime.datetime(**date)


if __name__ == '__main__':
    print(process_date('today'))
