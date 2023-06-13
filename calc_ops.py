import datetime

from input_processor import process_date


def process_datelapse(query):
    date, sign, lapse = query.split()
    date = process_date(date)
    lapse = datetime.timedelta(days=int(lapse))
    if '+' in sign:
        res = date + lapse
    elif '-' in sign:
        res = date - lapse
    else:
        raise RuntimeError(f"Wrong sign: {sign}; should be '+' or '-'")
    return res


def process_datedelta(query):
    date0, date1 = map(process_date, query.split())
    return abs(date1 - date0)


if __name__ == '__main__':
    process_datelapse('20 today')
