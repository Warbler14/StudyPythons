# -*- coding: utf-8 -*-

# set number to String
strData1 = str(12345)
print(strData1)

numberData = 1
numberData += 10
print(numberData)

numberData = 10 << 1
print(numberData)

numberData = 10 << 2
print(numberData)

numberData = 10 >> 1
print(numberData)

numberData = 10 >> 2
print(numberData)

list1 = ['one', 'two', 'three']
print(list1)
print(list1[0] + "," + list1[1] + "," + list1[2])

dictionaries1 = {"one": 1, "two": 2, "three": 3}
print(dictionaries1)
print(str(dictionaries1.get("one")) + "," + str(dictionaries1.get("two")) + "," + str(dictionaries1.get("three")))

tuple1 = ('one', "two", 'three')
print(tuple1)

strData = "Hello World"

print(strData[0])
print(strData[-1])
print(strData[1:2])
print(strData[0:])
print(strData[1:])
print(strData[:3])

splitStringData = strData.split(" ")
print(splitStringData)

print("--------------------------------")

testStr1 = "abcdefgh"

print(testStr1[::2])
print(testStr1[::2] * 3)
print(len(testStr1))

print("abc" in testStr1)
print("--------------------------------")

L = [1, 2, 3]
print(len(L))
print(L + L)

L.append(4)
print(L)
del L[0]
print(L)

L.reverse()
print(L)
L.sort()
print(L)

print(3 in L)

print("--------------------------------")
T = (1, 2, 3)
print(len(T))
print(T[0])
print(T[0:2])
print(T[::2])

print(T * 2)
print(T + T)
print(1 in T[1:2] + T[0:1])

TL = list(T)
print(TL)
LT = tuple(L)
print(LT)

print("--------------------------------")
TT = ((1, 2, 3), [4, 5, 6])
print(TT)
TTL = list(TT)
print(TTL)

LL = [[1, 2, 3], (4, 5, 6)]
print(LL)
LLT = tuple(LL)
print(LLT)

print("--------------------------------")
D = {"one": 1, "two": 2, "three": 3}
print(D)
print(D.get("one"))
print(D["one"])
print(D.keys())
print(D.values())
print(D.items())

print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))

value = {
    "top": 2000,
    "middle": 2000,
    "bottom": 2000
}
print(value)
for key in value.keys():
    print('key : ', key, ', value : ', value[key], end='||')
print()

print("--------------------------------")
string_text = "Python is Amazing"

print(string_text.lower())
print(string_text.upper())
print(string_text[0].isupper())
print(len(string_text))
print(string_text.replace("Python", "Java"))
# print(string_text)

index = string_text.index("n")
print(str(index))

index = string_text.index("n", index + 1)
print(str(index))

print(string_text.find("n"))
print(string_text.find("Java"))
# print(string_text.index("Java"))

print(string_text.count("n"))

number = 10
day = "three"
print("I eat %d apples." % number)
print("I ate %d apples. so I was sick for %s days." % (number, day))