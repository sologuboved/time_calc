from calculate_days import *
from calculate_hours import *

# TODO fix today to day
# TODO fix today and now to the appropriate timezone
# TODO substitute : for .
# TODO add /now
# TODO return input in addition to output
# TODO print out input & output

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

# print(date_after("today / 1"))
# print(date_after("today / 10"))
# print(date_before("11 / 10"))
# print(days_between("16 / 13"))
# print(days_between("14 / 15"))
print(days_between("today / 20"))

# print(calculate_time_sequence("17.12 + 1.10 - 5"))  # 0:18.17
# print(calculate_time_sequence("23.55.55 + 6.6 + 1"))  # 1 day, 0:02:02
# print(calculate_time_sequence("27.0 * 2"))  # 0:54:00
# print(calculate_time_sequence("1.56.17 - 8.0 - 1.0.0 + 0 + 20.7 - 1.0"))  # 1:07:24
# print(calculate_time_sequence("49.0.7 - 3.10.7 - 72.59.0 * 2 + 2 + 54.17.58"))  # 0:00:00

# print(time_after("13.12.2017 23.56.52 / 3.8"))  # 14 December 2017, Thursday 00:00:00
# print(time_after("13.12.2017 13.22.0/ 1.0"))  # 13 December 2017, Wednesday 13:23:00
# print(time_after("31.12.2017 0.0.1 / 23.59.59"))  # 01 January 2018, Monday 00:00:00
# print(time_after("13.12.2017 0.0.0 / 73.1.1"))  # 16 December 2017, Saturday 01:01:01
# print(time_after("14.12.2017 23.59.0 / 120"))  # 15 December 2017, Friday 00:01:00

# print(time_before("14.12.2017 0.10.0 / 48.11.0"))  # 11 December 2017, Monday 23:59:00

# print(time_between("now / 15.12.2017 0.0.0"))
# print(time_between("13.12.2017 12.28.0 / 12.12.2017 0.59.0"))  # 1 day, 11:29:00


