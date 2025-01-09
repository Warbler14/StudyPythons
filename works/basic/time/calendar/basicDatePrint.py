import datetime

from datetime import datetime as dt

now = dt.now()

print(now)
print(type(now))
print('년 : {}'.format(now.year))
print('월 : {}'.format(now.month))
print('일 : {}'.format(now.day))
print('시 : {}'.format(now.hour))
print('분 : {}'.format(now.minute))
print('초 : {}'.format(now.second))
print('마이크로초 : {0:06d}'.format(now.microsecond))
print('요일 : {}'.format(now.weekday()))

print('-'*20)

print(now.strftime('%Y-%m-%d'))
print(now.strftime('%y-%m-%d'))
print(now.strftime('%y-%B-%d'))
print(now.strftime('%y-%b-%d'))
print(now.strftime('%y-%b-%d %A'))
print(now.strftime('%y-%b-%d %a'))
print(now.strftime('%B %d %Y %H: %M: %S'))