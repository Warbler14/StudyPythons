# -*- coding: utf-8 -*-

def print_reverse(text):
    print(text[::-1])

print_reverse("python")

def print_score(list_data):
    result = 0
    for number in list_data:
        result += number
    print(result / len(list_data))


def print_score2(score_list):
    print(sum(score_list)/len(score_list))

print_score([1, 2, 3])

print()
def print_even(list_data):
    for number in list_data:
        if number % 2 == 0:
            print(number)

print_even([1, 3, 2, 10, 12, 11, 15])


print()
def print_keys(dic):
    if isinstance(dic, dict):
        for key in dic.keys():
            print(key)


print_keys({"이름": "김말똥", "나이": 30, "성별": 0})


my_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]}

def print_value_by_key(dic, key):
    if not isinstance(dic, dict):
        None
    if not isinstance(key, str):
        None
    print(dic[key])


print_value_by_key(my_dict, "10/26")


def print_5xn(string):
    if not isinstance(string, str):
        None

    word = ""
    for idx in range(len(string)):
        word += string[idx]
        if len(word) == 5:
            print(word)
            word = ""
    if word != "":
        print(word)


print_5xn("아이엠어보이유알어걸지지")

print()
def print_mxn(string, word_length):
    if not isinstance(string, str):
        None
    if not isinstance(word_length, int):
        None

    word = ""
    for idx in range(len(string)):
        word += string[idx]
        if len(word) == word_length:
            print(word)
            word = ""
    if word != "":
        print(word)


print_mxn("아이엠어보이유알어걸", 3)

print()
def calc_monthly_salary(annual_salary):
    return int(annual_salary / 12)

print(calc_monthly_salary(12000000))

print()
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

print()
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)