# -*- coding: utf-8 -*-
# 테스트 2017-11-06

dataList = [1, 2, 3, 4, 5]

for item in dataList:
    print(item)


def hap(a, b):
    print(a + b)


hap(100, 200)


def print_hello():
    print('Hello')


print_hello()


def countdown(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


countdown(10)


print('구구단 출력')

i = 2
while i <= 9:
    j = 1
    while j <= 9:
        print(str(i) + ' * ' + str(j) + ' = ' + str(i * j))
        j = j + 1
    i = i + 1


def multi(dan):
    var = 1

    while var <= 9:
        print(str(dan) + ' * ' + str(var) + ' = ' + str(dan * var))
        var = var + 1


multi(5)
