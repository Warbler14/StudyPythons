# -*- coding: utf-8 -*-

print("-=-261-=-")
class Stock:
    pass

print("-=-262-=-")
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)

print("-=-263-=-")
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)

print("-=-264-=-")
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

a = Stock(None, None)
a.set_code("005930")
print(a.code)

print("-=-265-=-")
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

삼성 = Stock("삼성전자", "005930")
print(삼성.get_name())
print(삼성.get_code())

print("-=-266-=-")
class Stock:
    def __init__(self, name, code, PER, PBR, 배당수익률):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률


print("-=-267-=-")
삼성전자 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성전자.배당수익률)

print("-=-268-=-")
class Stock:
    def __init__(self, name, code, PER, PBR, 배당수익률):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, PER):
        self.PER = PER

    def set_pbr(self, PBR):
        self.PBR = PBR

    def set_dividend(self, 배당수익률):
        self.배당수익률 = 배당수익률


print("-=-269-=-")
samsung_electronics = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(samsung_electronics .PER)
samsung_electronics.set_per(12.75)
print(samsung_electronics .PER)

print("-=-270-=-")
stocks = [
    Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
    , Stock("현대차", "005380", 8.70, 0.35, 4.27)
    , Stock("LG전자", "066570", 317.34, 0.69, 1.37)]

for stock in stocks:
    print(stock.name, stock.PER)
