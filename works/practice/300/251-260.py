# -*- coding: utf-8 -*-

print("-=-251-=-")
print("객체는 어떠한 속성값과 행동을 가지고있는 데이터")
print("클래스는 설계도이며 객체를 표현하기 위한 문법, 속성과 메소드로 구분된다.")
print("인스턴스는 클래스를 이용하여 생성된 실체")

print("-=-252-=-")
class Human:
    pass

print("-=-253-=-")
areum = Human()

print(type(areum))

print("-=-254-=-")

class Human:
    def __init__(self):
        print("응애응애")

areum = Human()

print("-=-255-=-")
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
print(areum.name)

print("-=-256-=-")
print("이름: {}, 나이: {}, 성별: {}".format(areum.name, areum.age, areum.sex))

print("-=-257-=-")
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))

areum = Human("조아름", 25, "여자")
areum.who()

print("-=-258-=-")
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))

areum = Human("모름", 0, "모름")
areum.setInfo("강아름", 26, "여자")
areum.who()

print("-=-259-=-")
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))

    def myId(self):
        print(id(self))

    def __del__(self):
        print("나의 죽음을 알리지 말라")


areum = Human("아름", 25, "여자")
areum.myId()
print(id(areum))
del areum

print("-=-260-=-")
# class OMG :
#     def print():            #self 없음
#         print("Oh my god")
#
# myStock = OMG()
# myStock.print()
