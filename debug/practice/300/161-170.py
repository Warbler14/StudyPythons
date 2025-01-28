# -*- coding: utf-8 -*-

# for number in range(0, 100):
#     print(number)
# for number in range(100):
#     print(number)

for year in range(2002, 2050, 4):
    print(year)

print()
for number in range(3, 31, 3):
    print(number)

# print()
# for number in range(99, -1, -1):
#     print(number)

print()
for number in range(10):
    print("{:.1f}".format(number * 0.1))

print()
divisor = 3
for number in range(1, 10):
    print("{}x{} = {}".format(divisor, number, divisor * number))

print()
divisor = 3
for number in range(1, 10):
    if number % 2 == 1:
        print("{}x{} = {}".format(divisor, number, divisor * number))

print()
sum = 0
for number in range(1, 11):
    sum += number
print(sum)

print()
sum = 0
for number in range(1, 11):
    if number % 2 == 1:
        sum += number
print(sum)

print()
result = 1
for number in range(1, 11):
    result *= number
print(result)

