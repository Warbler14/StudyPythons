# -*- coding: utf-8 -*-

letters = 'python'
print(letters[0], letters[2])

license_plate = "24가 2210"
print(license_plate[4:])

string = "홀짝홀짝홀짝"
print(string[0] + string[2] + string[4])
print(string[::2])

string = "PYTHON"
print(string[::-1])

phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

print(phone_number.replace("-", ""))

url = "http://sharebook.kr"
print(url[url.index('.') + 1:])
url_split = url.split('.')
print(url_split[-1])

'''
lang = 'python'
lang[0] = 'P'   # TypeError: 'str' object does not support item assignment
print(lang)
'''

string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

string = 'abcd'
string2 = string.replace('b', 'B')
print(string, string2)   # abcd
