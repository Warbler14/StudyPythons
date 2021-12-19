# -*- coding: utf-8 -*-

class FourCal:
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



a = FourCal()
print(type(a))      # <class '__main__.FourCal'>

b = FourCal()
b.setdata(22, 7)
print(b.first, b.second)
print('add :', b.add())
print('mul :', b.mul())
print('sub :', b.sub())
print('div :', b.div())
