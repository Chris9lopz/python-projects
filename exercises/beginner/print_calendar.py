# Exercise print a calendar for a year and specific day

import calendar

year = int(input('Please enter the year: '))
month = int(input('Please enter the month: '))

print(calendar.month(year, month))
