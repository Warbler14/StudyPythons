# -*- coding: utf-8 -*-

from random import randint
from random import random
from random import randrange
from random import sample

print('0.0 ~ 1.0 미만의 임의의 값 ', random())
print('0.0 ~ 10.0 미만의 임의의 값 ', random() * 10)

print('1 ~ 10 이하의 임의의 값')
for i in range(1, 10):
    print(int(random() * 10), end=', ')
print()

print('1 ~ 46 미만의 임의의 값 생성')
for i in range(1, 10):
    print(randrange(1, 46), end=', ')
print()

print('1 ~ 45 이하의 임의의 값 생성')
for i in range(1, 10):
    print(randint(1, 45), end=', ')
print()

list1 = [1, 2, 3, 4, 5]
for i in range(1, 10):
    print(sample(list1, 2), end=', ')
print()
