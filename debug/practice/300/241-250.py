# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import time
import os
import numpy

print("-=-241-=-")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print(datetime.now())

print("-=-242-=-")
print(now, type(datetime.now()))

print("-=-243-=-")
print(type(timedelta(days=7)))

print()
for day in range(5, 0, -1):
    delta = timedelta(days=day)
    date = now - delta
    print(date)

print("-=-244-=-")
print(datetime.now().strftime("%H:%M:%S"))

print("-=-245-=-")
ret = datetime.strptime("2020-05-04", "%Y-%m-%d")
print(ret, type(ret))

print("-=-246-=-")
for idx in range(2):
    time.sleep(1)
    now = datetime.now()
    print(now)

print("-=-247-=-")
print("import lib, from lib import x, from lib import *")
print(dir())

print("-=-248-=-")
print(os.getcwd())

print("-=-249-=-")
if os.path.exists("test.txt"):
    os.rename("test.txt", "test1.txt")
elif os.path.exists("test1.txt"):
    os.rename("test1.txt", "test.txt")

print("-=-250-=-")
for num in numpy.arange(0.0, 0.5, 0.1):
    print(num)
