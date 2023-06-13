def output_timelet(timelet):
    return f"{timelet:%H:%M:%S}"


def output_date(date):
    return f"{date:%d.%m.%Y}"


def output_days(delta):
    days = delta.days
    if days == 1:
        postfix = ''
    else:
        postfix = 's'
    return f"{days} day{postfix}"
