from process_hours import *


def calculate_time_series(user_input):
    # raw timelet {+, -, *} raw timelet ...
    processed_series = process_time_series(user_input)
    if not processed_series:
        return INVALID_INPUT

    first_timelet = processed_series[0]
    curr_res = convert_to_secs(*first_timelet)
    print(curr_res)

    ind = 1
    while ind + 1 < len(processed_series):
        sign = processed_series[ind]
        print(sign, end=" ")
        print(processed_series[ind + 1])

        if sign == PLUS:
            curr_res += convert_to_secs(*processed_series[ind + 1])
        elif sign == MINUS:
            curr_res -= convert_to_secs(*processed_series[ind + 1])
        elif sign == ASTERIX:
            curr_res *= processed_series[ind + 1]
        ind += 2
        print('= ', curr_res)

    return process_time_output(convert_to_dhms(curr_res), delta=True)


def time_after(user_input):
    # raw date raw timelet / raw timelet
    date, timelet, lapse = process_timelapse(user_input)


def time_before(user_input):
    # raw date raw timelet / raw timelet
    date, timelet, lapse = process_timelapse(user_input)


def time_between(user_input):
    # raw date raw timelet / raw date raw timelet
    start_date, start_time, end_date, end_time = process_timetime(user_input)


if __name__ == '__main__':
    # time_after("17 17.14.0 / 2.35.07")
    # time_after("17 17.a.0 / 2.35.07")
    time_between("17 now / 20.12 2.65.07")

