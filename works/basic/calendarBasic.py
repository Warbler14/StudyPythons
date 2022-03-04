# -*- coding: utf-8 -*-

# from datetime import date
# from calendra.asia import south_korea
import sys
import calendar

print(sys.version)

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


print('-------------------------------')

print(0, is_leap_year(0))
print(1, is_leap_year(1))
print(4, is_leap_year(4))
print(1200, is_leap_year(1200))
print(900, is_leap_year(700))
print(2020, is_leap_year(2020))

print('-------------------------------')
# calendar.iterweekdays()

print('-------------------------------')
print(0, calendar.isleap(0))
print(1, calendar.isleap(1))
print(4, calendar.isleap(4))
print(1200, calendar.isleap(1200))
print(900, calendar.isleap(700))
print(2020, calendar.isleap(2020))
