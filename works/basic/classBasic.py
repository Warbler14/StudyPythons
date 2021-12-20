# -*- coding: utf-8 -*-

class FourCal:
    def __init__(self, first, second):
        self.setdata(first, second)
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = FourCal(1, 2)
print(type(a))      # <class '__main__.FourCal'>

print('--- FourCal ---')
b = FourCal(22, 7)
b.setdata(22, 7)
print(b.first, b.second)
print('add :', b.add())
print('mul :', b.mul())
print('sub :', b.sub())
print('div :', b.div())

print('--- MoreFourCal ---')
c = MoreFourCal(22.0, 7.0)
print(c.first, c.second)
print('add :', c.add())
print('mul :', c.mul())
print('sub :', c.sub())
print('div :', c.div())
print('pow :', c.pow())

print('--- SafeFourCal ---')
d = SafeFourCal(10, 0)
print('div :', d.div())
