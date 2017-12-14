from process_days_input import *
from process_output import *


def date_after(user_input):
    # raw date DELIMITER raw lapse
    date, lapse = process_datelapse(user_input)
    if not (date and lapse):
        return INVALID_INPUT
    try:
        return process_date_ouput(date + lapse, False)
    except OverflowError:
        return INVALID_INPUT


def date_before(user_input):
    # raw date DELIMITER raw lapse
    date, lapse = process_datelapse(user_input)
    if not (date and lapse):
        return INVALID_INPUT
    try:
        return process_date_ouput(date - lapse, False)
    except OverflowError:
        return INVALID_INPUT


def days_between(user_input):
    # raw date DELIMITER raw date
    try:
        start, end = map(lambda u: u.replace(hour=0, minute=0, second=0, microsecond=0), process_datedate(user_input))
    except AttributeError:
        return INVALID_INPUT
    try:
        return process_date_ouput(abs(end - start), True)
    except OverflowError:
        return INVALID_INPUT
