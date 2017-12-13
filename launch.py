from calculate_days import *
from calculate_hours import *

"""
raw date:
'today'
'11.12.2017' [11 December 2017]
'11.12' [11 December same year as today]
'11' [11 same month and year as today]

raw lapse:
'10' [10 days]

raw timelet:
'now'
'21.11.12' [21:11:12]
'11.12' [00:11:12]
'12' [00:00:12]
"""

# TODO 1 day, 0:2.2 --> 1 day, 00:02.2

# print(date_after("today / 10"))
# print(date_before("11 / 10"))
# print(days_between("13.12 / 1. 3. 2018"))

# print(calculate_time_series("17.12 + 1.10 - 5"))  # 0:18.17
# print(calculate_time_series("23.55.55 + 6.6 + 1"))  # 24:2.2
# print(calculate_time_series("27.0 * 2"))  # 0:54.0
# print(calculate_time_series("1.56.17 - 8.0 - 1.0.0 + 0 + 20.7 - 1.0"))  # 1:7.24
# print(calculate_time_series("49.0.7 - 3.10.7 - 72.59.0 * 2 + 2 + 54.17.58"))  # 0:0.0

# print(time_after("today 23.56.52 / 3.8"))
# print(time_after("now / 1.0"))
# print(time_after("31 1 / 23.59.59"))
# print(time_after("13.12.2017 0.0.0 / 73.1.1"))
# print(time_after("14.12.2017 23.59.0 / 120"))

print(time_before("14.12.2017 0.10.0 / 48.11.0"))


