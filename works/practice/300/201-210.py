# -*- coding: utf-8 -*-

def print_coin():
    print("비트코인")


print_coin()

# for idx in range(100):
#     print_coin()


def print_coins():
    for idx in range(100):
        print_coin()


# print_coins()

def message():
    print("A")
    print("B")


message()
print("C")
message()

print()
print("A")


def message2():
    print("B")


print("C")
message2()

print()
print("A")
def message3():
    print("B")
print("C")
def message4():
    print("D")
message3()
print("E")
message4()

print()
def message5():
    print("A")
def message6():
    print("B")
    message5()
message6()

print()
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range(3):
        message2()
        print("C")
    message1()

message3()