from calculate_days import *
from process_hours import *

"""
raw date:
'today'
'11 12 2017' [11 December 2017]
'11 12' [11 December same year as today]
'11' [11 same month and year as today]

raw lapse:
'10' [10 days]

raw timelet:
'now'
'21 11 12' [21:11:12]
'11 12' [00:11:12]
'12' [00:00:12]
"""

# TODO input: date time, lapse; output: time after lapse
# TODO input: date time, lapse; output: time before lapse

print(after("today / 10"))
print(before("11 / 10"))
print(between("today / 1 3 2018"))

print(process_time_output(process_time_series("17.12 + 1.10 - 5"), delta=True))
print(process_time_output(process_time_series("23.55.55 + 6.6 + 1"), delta=True))
print(process_time_output(process_time_series("27.0 * 2"), delta=True))
print(process_time_output(process_time_series("1.56.17 - 8.0 - 1.0.0 + 0 + 20.7 - 1.0"), delta=True))

