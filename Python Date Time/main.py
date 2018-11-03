# 1. Write a Python script to display the - Go to the editor
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
import datetime
dt = datetime.datetime.today()
# dt_d = datetime.datetime.weekday()
# print(dt_d)
print(f'Current {dt.date()} and {dt.time()}')
print(f'Current {dt.year}')
print(f'{dt.month} of {dt.year}')
print(f'week number of the {dt.year}')
print(f'{dt.weekday()} weekday of the week')
print(f'{dt.day} of {dt.year}')
print(f'{dt.day} of the {dt.month}')
print(f'{dt.day} of week')