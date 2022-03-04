# -*- coding: utf-8 -*-

import datetime

day1 = datetime.date(2022, 2, 12)
day2 = datetime.date(1983, 1, 11)
print(day1, day1.weekday(), day2, day2.weekday())

diff = day1 - day2
print('diff days : ', diff.days)


def print_datetime(date_time):
    print('-------------------------------')
    print('year : ', date_time.year)
    print('month : ', date_time.month)
    print('day : ', date_time.day)
    print('hour : ', date_time.hour)
    print('minute : ', date_time.minute)
    print('second : ', date_time.second)
    print('weekday : ', date_time.weekday())
    print('isoweekday : ', date_time.isoweekday())
    print('-------------------------------')


day3 = datetime.datetime(2022, 2, 12, 23, 44, 5)
print_datetime(day3)

day4 = datetime.datetime(2022, 2, 13, 0, 0, 5)
print_datetime(day4)

today = datetime.date.today();
print(today)

