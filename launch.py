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

# TODO input: date time, lapse; output: time before lapse
# TODO 1 day, 0:2.2 --> 1 day, 00:02.2
# TODO -0 in days - fix bug

# print(date_after("today / 10"))
# print(date_before("11 / 10"))
# print(days_between("13.12 / 1. 3. 2018"))

# print(calculate_time_series("17.12 + 1.10 - 5"))  # 0 days, 0:18.17
# print(calculate_time_series("23.55.55 + 6.6 + 1"))  # 1 day, 0:2.2
# print(calculate_time_series("27.0 * 2"))  # 0 days, 0:54.0
# print(calculate_time_series("1.56.17 - 8.0 - 1.0.0 + 0 + 20.7 - 1.0"))  # 0 days, 1:7.24
# print(calculate_time_series("2.1.0.7 - 3.10.7 - 3.0.59.0 * 2 + 2 + 2.6.17.58"))  # 0 days, 0:0.0

# print(time_after("today 23.56.52 / 3.8"))
# print(time_after("now / 1.0"))
# print(time_after("31 1 / 23.59.59"))
# print(time_after("3.0 / 3.1.1.1"))

print(time_before("37.52 / 40.0"))
# print(time_before("3.0 / 3.0.1.0"))
print(convert_to_dhms(-128))
