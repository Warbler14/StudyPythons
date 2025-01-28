# -*- coding: utf-8 -*-


boolVal = True
print(boolVal, type(boolVal))

print(3 == 5)

print(3 < 5)

x = 4
print(1 < x < 5)

print((3 == 3) and (4 != 3))

if 4 < 3:
    print("Hello World")

if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

if True:
    print("1")
    print("2")
else:
    print("3")
print("4")

print('-----')

if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
