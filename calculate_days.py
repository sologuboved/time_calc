from process_days import *


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
    start, end = process_datedate(user_input)
    if not (start and end):
        return INVALID_INPUT
    try:
        return process_date_ouput(abs(end - start), True)
    except OverflowError:
        return INVALID_INPUT
