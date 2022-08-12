# -*- coding: utf-8 -*-
# 테스트 2017-11-09


def sum_data(a, b):
    return a + b


c = sum_data(1, 2)
print(c)


def sum_many(*args):
    result = 0
    for idx in args:
        result = result + idx
    return result


resultData = 0

resultData = sum_many(1)
print(resultData)
resultData = sum_many(1, 2)
print(resultData)
resultData = sum_many(1, 2, 3)
print(resultData)
resultData = sum_many(1, 2, 3, 4)
print(resultData)
resultData = sum_many(1, 2, 3, 4, 5)
print(resultData)


def sum_and_mul(a, b):
    return a+b, a*b


resultSumAndMul = sum_and_mul(10, 100)
print(resultSumAndMul)
