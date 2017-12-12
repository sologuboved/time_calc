from calculate_days import *

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

# TODO input: lapse1, lapse2, lapse3, ...; output: sum
# TODO input: date time, lapse; output: time after lapse
# TODO input: date time, lapse; output: time before lapse

print(after("today / 10"))
print(before("11 / 10"))
print(between("today / 1 3 2018"))

