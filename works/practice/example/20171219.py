# -*- coding: utf-8 -*-
# 테스트 2017-12-19


result = 0


def adder(num):
    global result
    result += num
    return result


print(adder(3))
print(adder(4))

print("~~~~~~~~~~~~~~ test class ~~~~~~~~~~~~~~")
# 클래스


class Calculator:
    def __init__(self):
        self.result = 0

    def __del__(self):
        print("remove Calculator")

    def adder(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal1.sub(5))

print(cal2.adder(3))
print(cal2.adder(7))
print(cal2.sub(4))


print("~~~~~~~~~~~~~~ test class ~~~~~~~~~~~~~~")


class FourCal:
    def __init__(self):
        self.result = 0
        self.num1 = 0
        self.num2 = 0

    def setnumber(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        self.result += self.num1
        self.result += self.num2
        return self.result

    def sub(self):
        self.result += self.num1
        self.result -= self.num2
        return self.result

    def mul(self):
        self.result += self.num1
        self.result * self.num2
        return self.result

    def div(self):
        self.result += self.num1
        self.result / self.num2
        return self.result


cal1 = FourCal()
cal1.setnumber(5, 10)
print(cal1.sum())

cal1.setnumber(5, 10)
print(cal1.sub())

cal1.setnumber(10, 5)
print(cal1.mul())

cal1.setnumber(10, 5)
print(cal1.div())
