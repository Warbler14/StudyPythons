# -*- coding: utf-8 -*-
import math


def sqrt(n):
    return math.sqrt(n)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for number in numbers:
        print(number, ':', math.sqrt(number))
