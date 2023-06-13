import datetime

from input_processor import process_date, process_timelet


def process_timelets(query):
    res = datetime.timedelta()
    previous_sign = '+'
    for item in map(str.strip, query.split()):
        if item in ('+', '-', '*', '/'):
            previous_sign = item
        else:
            item = process_timelet(item)
            if previous_sign == '+':
                res += item
            elif previous_sign == '-':
                res -= item
            elif previous_sign == '*':
                res *= item
            elif previous_sign == '/':
                res /= item
            else:
                raise RuntimeError(f"Wrong sign: {item}; should be '+', or '-', or '*', or '/'")
    return res


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
    print(process_timelets('1:30 + 10 * 2'))
