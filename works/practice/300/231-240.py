# -*- coding: utf-8 -*-

def n_plus_1(n):
    return n + 1

print (n_plus_1(3))

def make_url(domain):
    return "www." + domain + ".com"

print(make_url("naver"))

def make_list(string):
    return list(string)

print(make_list("abcd"))

def pickup_even(list_data):
    result = []
    for number in list_data:
        if number % 2 == 0:
            result.append(number)
    return result

print(pickup_even([3, 4, 5, 6, 7, 8]))

def convert_int(number_string):
    result = number_string.replace(",", "")
    return int(result)

print(convert_int("1,234,567"))

def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)




def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
