def output_timelet(timelet):
    return str(timelet)


def output_date(date):
    return f"{date:%d.%m.%Y, %a}"


def output_datetimelet(datetimelet, include_date):
    if include_date:
        return f"{datetimelet:%d.%m.%Y, %a %H:%M}"
    else:
        return f"{datetimelet:%H:%M}"


def output_days(delta):
    days = delta.days
    if days == 1:
        postfix = ''
    else:
        postfix = 's'
    return f"{days} day{postfix}"


def output_dow(date):
    return f'{date:%a}!'


def output_num(num):
    return str(num)
