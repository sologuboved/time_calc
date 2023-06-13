import datetime

from input_processor import process_date


def process_dateday(query):
    date, sign, delta = query.split()
    date = process_date(date)
    delta = datetime.timedelta(days=int(delta))
    if '+' in sign:
        res = date + delta
    elif '-' in sign:
        res = date - delta
    else:
        raise RuntimeError(f"Wrong sign: {sign}; should be '+' or '-'")
    return res


def process_datedate(query):
    date0, date1 = map(process_date, query.split())
    return abs(date1 - date0)


if __name__ == '__main__':
    process_dateday('20 today')
