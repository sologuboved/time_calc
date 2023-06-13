import datetime

from input_processor import process_date


def process_datedelta(query):
    date, sign, delta = map(str.strip, query.split())
    date = process_date(date)
    delta = datetime.timedelta(days=int(delta))
    if sign == '+':
        res = date + delta
    elif sign == '-':
        res = date - delta
    else:
        raise RuntimeError(f"Wrong sign: {sign}; should be '+' or '-'")
    return res
