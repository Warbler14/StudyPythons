# -*- coding: utf-8 -*-
# 테스트 2017-11-02
import random

num = 1
while num < 100:
    print(num)
    num = num + 1


print('-----------------\n')

num = 1
while num < 100:
    print(num),

    if num % 2 == 0:
        print('-even number-')
    else:
        print('-odd number-')

    num = num + 1

print('-----------------\n')

num = 1
while num < 100:
    randomNumber = random.randrange(0, 10)
    print('num : %i, randomNumber : %i' % (num, randomNumber))

    num = num + 1


