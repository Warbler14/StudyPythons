# -*- coding: utf-8 -*-
# 테스트 2017-11-20


def hap(x, y):
    return x+y


hap1 = hap(10, 20)

print(hap1)


hap2 = (lambda x, y: x+y)(10, 20)

print(hap2)

# --------------------------------------

list1 = map(lambda x: x ** 2, range(5))

print(list1)


list2 = list(map(lambda x: x ** 2, range(5)))

print(list2)


# --------------------------------------
# 내장함수
# --------------------------------------

# abs : abs(x)는 어떤 숫자를 입력으로 받았을 때, 그 숫자의 절대값을 돌려주는 함수이다.

print("==============================================")
print("test abs(x)")
print("==============================================")

print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all(x) 은 반복 가능한(iterable) 자료형 x를 입력 변수로 받으며
# , 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False 를 리턴한다.

print("==============================================")
print("test all()")
print("==============================================")

print(all([1, 2, 3]))

print(all([1, 2, 3, 0]))

print(all([1, 2, 3, ""]))


# any(x) 는 x 중 하나라도 참이 있을 경우 True 를 리턴하고,
# x가 모두 거짓일 경우에만 False 를 리턴한다.

print("==============================================")
print("test any([1, 2, 3])")
print("==============================================")

print(any([1, 2, 3]))

print(any([1, 2, 3, 0]))

print(all([1, 2, 3, ""]))

print(all([0, 0]))

print(all([0, ""]))

print(all(["", 0]))

print(all(["", ""]))

# chr(i) 는 아스키(ASCII) 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력하는 함수이다.

print("==============================================")
print("test chr(97)")
print("==============================================")

for dec in range(48, 58, 1):
    print(chr(dec))

for dec in range(65, 91, 1):
    print(chr(dec))

for dec in range(97, 123, 1):
    print(chr(dec))


# dir 은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.

print("==============================================")
print("test dir")
print("==============================================")

print(dir([1, 2, 3]))
print(dir({'1': 'a'}))

