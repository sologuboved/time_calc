from process_hours import *


def calculate_time_series(user_input):
    res = process_time_series(user_input)
    if res is None:
        return INVALID_INPUT
    return process_time_output(res, delta=True)


# def


if __name__ == '__main__':
    pass
