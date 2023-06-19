import datetime

from input_processor import process_date, process_datetimelet, process_timelapse


def process_timelapses(query):
    res = datetime.timedelta()
    previous_sign = '+'
    for item in map(str.strip, query.split()):
        if item in ('+', '-', '*', '/'):
            previous_sign = item
        else:
            if previous_sign == '+':
                item = process_timelapse(item, zero_seconds=False)
                res += item
            elif previous_sign == '-':
                item = process_timelapse(item, zero_seconds=False)
                res -= item
            elif previous_sign == '*':
                item = int(item)
                res *= item
            elif previous_sign == '/':
                item = int(item)
                res /= item
            else:
                raise RuntimeError(f"Wrong sign: {item}; should be '+', or '-', or '*', or '/'")
    return res


def process_datelapse(query):
    date, sign, daylapse = query.split()
    date = process_date(date)
    daylapse = datetime.timedelta(days=int(daylapse))
    if '+' in sign:
        res = date + daylapse
    elif '-' in sign:
        res = date - daylapse
    else:
        raise RuntimeError(f"Wrong sign: {sign}; should be '+' or '-'")
    return res


def process_datedelta(query):
    query = query.replace('-', ' ')
    dates = list(map(process_date, query.split()))
    return max(dates) - min(dates)


def process_howmany(query):
    query = list(map(str.strip, query.split()))
    if len(query) == 3:
        dow, beg, fin = query
    elif len(query) == 2:
        beg = 'today'
        dow, fin = query
    else:
        raise RuntimeError(f"Wrong input: should include 1 or 2 dates & day of week")
    beg, fin = (process_date(date) for date in (beg, fin))
    daylapse = (fin - beg).days
    res = daylapse // 7
    remainder = daylapse % 7
    remaining_date = fin - datetime.timedelta(days=remainder)
    while remaining_date <= fin:
        if remaining_date.strftime('%a') == dow:
            res += 1
            break
        remaining_date += datetime.timedelta(1)
    return res


def process_datetimelapse(query):
    query = query.split()
    if len(query) == 4:
        print_date = True
        date, timelet, sign, timelapse = query
    elif len(query) == 3:
        print_date = False
        timelet, sign, timelapse = query
        date = 'today'
    else:
        raise RuntimeError(f"Wrong input: should include (optional) date, time, sign, and time lapse")
    datetimelet = process_datetimelet(date, timelet)
    timelapse = process_timelapse(timelapse, zero_seconds=True)
    if '+' in sign:
        res = datetimelet + timelapse
    elif '-' in sign:
        res = datetimelet - timelapse
    else:
        raise RuntimeError(f"Wrong sign: {sign}; should be '+' or '-'")
    if res.day != datetimelet.day:
        print_date = True
    return res, print_date


def process_datetimedelta(query):
    beg, fin = query.split('-')
    datetimelets = list()
    for datetimelet in (beg, fin):
        datetimelet = datetimelet.split()
        if len(datetimelet) == 1:
            datetimelets.append(process_datetimelet('today', datetimelet))
        else:
            datetimelets.extend(process_datetimelet(*datetimelet))
    return max(datetimelets) - min(datetimelets)


if __name__ == '__main__':
    print(process_howmany("today 26 Sat"))
