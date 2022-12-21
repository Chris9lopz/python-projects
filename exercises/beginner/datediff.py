# Exercise calculate the difference between two dates

from datetime import datetime


def datediff(date1, date2):

    date_first = datetime.strptime(date1, '%Y/%m/%d')
    date_second = datetime.strptime(date2, '%Y/%m/%d')

    result = date_first - date_second

    return result


date_str1 = input('Please enter a date delimited by "/":')
date_str2 = input('Please enter a date delimited by "/":')

result = datediff(date_str1, date_str2)

print(f'The difference is {result}')
