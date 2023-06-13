def process_date(date):
    return f"{date:%d.%m.%Y}"


def process_days(delta):
    days = delta.days
    if days == 1:
        postfix = ''
    else:
        postfix = 's'
    return f"{days} day{postfix}"
