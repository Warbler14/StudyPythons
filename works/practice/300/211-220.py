# -*- coding: utf-8 -*-

def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

def print_with_smile(문자열):
    print(str(문자열) + ":)")

print_with_smile("hi")
print_with_smile("안녕하세요")

def print_upper_price(price):
    print(price * 1.3)

print_upper_price(10000)

def print_sum(a, b):
    print(a + b)

def print_arithmetic_operation(a, b):
    print("{} + {} = {}".format(a, b, a + b))
    print("{} - {} = {}".format(a, b, a - b))
    print("{} * {} = {}".format(a, b, a * b))
    print("{} / {} = {}".format(a, b, a / b))

print_arithmetic_operation(3, 4)

def print_max(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    print(max)

print_max(11, 15, 14)