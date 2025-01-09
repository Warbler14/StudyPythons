from calendar import *
from datetime import datetime as dt

now = dt.now()

print(now)
print(type(now))
print('년 : {}'.format(now.year))

print(calendar(now.year))

print('*'*20)

print(prmonth(now.year, now.month))