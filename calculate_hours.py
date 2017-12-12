import datetime
from process_hours_input import *
from process_output import *


def calculate_time_series(user_input):
    # raw timelet {+, -, *} raw timelet ...
    processed_series = process_time_series(user_input)
    if not processed_series:
        return INVALID_INPUT

    first_timelet = processed_series[0]
    curr_res = convert_to_secs(*first_timelet)

    ind = 1
    while ind + 1 < len(processed_series):
        sign = processed_series[ind]

        if sign == PLUS:
            curr_res += convert_to_secs(*processed_series[ind + 1])
        elif sign == MINUS:
            curr_res -= convert_to_secs(*processed_series[ind + 1])
        elif sign == ASTERIX:
            curr_res *= processed_series[ind + 1]
        ind += 2

    return process_time_output(convert_to_dhms(curr_res), with_days=True)


def time_after(user_input):
    # raw date raw timelet / raw timelet
    date, initial_timelet, lapse = process_timelapse(user_input)
    if not (date and initial_timelet and lapse):
        return INVALID_INPUT

    days, hrs, mins, secs = convert_to_dhms(convert_to_secs(*initial_timelet) + convert_to_secs(*lapse))
    date += datetime.timedelta(days)

    return process_date_ouput(date, delta=False) + " " + process_time_output((hrs, mins, secs), with_days=False)


def time_before(user_input):
    # raw date raw timelet / raw timelet
    date, initial_timelet, lapse = process_timelapse(user_input)
    if not (date and initial_timelet and lapse):
        return INVALID_INPUT

    days, hrs, mins, secs = convert_to_dhms(convert_to_secs(*initial_timelet) - convert_to_secs(*lapse))
    print(initial_timelet)
    print(lapse)
    print(hrs, mins, secs)
    date -= datetime.timedelta(abs(days))
    # date += datetime.timedelta(days)

    return process_date_ouput(date, delta=False) + " " + process_time_output((hrs, mins, secs), with_days=False)


def time_between(user_input):
    # raw date raw timelet / raw date raw timelet
    start_date, start_time, end_date, end_time = process_timetime(user_input)
    if not (start_date and start_time and end_date and end_time):
        return INVALID_INPUT
