# -*- coding: utf-8 -*-

리스트 = [3, -20, -3, 44]
for number in 리스트:
    if number < 0:
        print(number)

print()

리스트 = [3, 100, 23, 44]
for number in 리스트:
    if number % 3 == 0:
        print(number)

print()

리스트 = [13, 21, 12, 14, 30, 18]
for number in 리스트:
    if number % 3 == 0 and number < 20:
        print(number)

print()

리스트 = ["I", "study", "python", "language", "!"]
for word in 리스트:
    if len(word) >= 3:
        print(word)

print()

리스트 = ["A", "b", "c", "D"]
for character in 리스트:
    if character.isupper():
        print(character)

print()

리스트 = ["A", "b", "c", "D"]
for character in 리스트:
    if character.islower():
        print(character)

print()

리스트 = ['dog', 'cat', 'parrot']
for animal in 리스트:
    print(animal.capitalize())

print()

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for fileName in 리스트:
    print(fileName.split(".")[0])

print()

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for fileName in 리스트:
    split = fileName.split(".")
    if "h" == split[1]:
        print(fileName)

print()

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for fileName in 리스트:
    split = fileName.split(".")
    if split[1] in ["c", "h"]:
        print(fileName)
