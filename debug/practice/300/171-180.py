# -*- coding: utf-8 -*-

price_list = [32100, 32150, 32000, 32500]
for idx in range(len(price_list)):
    print(price_list[idx])

print()
price_list = [32100, 32150, 32000, 32500]
for idx in range(len(price_list)):
    print(idx, price_list[idx])

print()
price_list = [32100, 32150, 32000, 32500]
price_list_length = len(price_list)
for idx in range(price_list_length):
    print((price_list_length - 1) - idx, price_list[idx])

print()
price_list = [32100, 32150, 32000, 32500]
number = 100
for idx in range(3):
    print(number, price_list[idx])
    number += 10

print()
my_list = ["가", "나", "다", "라"]
for idx in range(3):
    for item in my_list[idx: idx + 2: 1]:
        print(item, end=" ")
    print()

print()
for idx in range(1, len(my_list)):
    print(my_list[idx-1], my_list[idx])

print()
my_list = ["가", "나", "다", "라", "마"]
for idx in range(2, len(my_list)):
    print(my_list[idx - 2], my_list[idx - 1], my_list[idx])

print()
my_list = ["가", "나", "다", "라"]
for idx in range(len(my_list)-1, 0, -1):
    print(my_list[idx], my_list[idx - 1])

print()
my_list = [100, 200, 400, 800]
for idx in range(len(my_list) - 1):
    print(my_list[idx + 1] - my_list[idx])

print()
my_list = [100, 200, 400, 800, 1000, 1300]
for idx in range(len(my_list) - 2):
    buffer = 0
    for idy in range(3):
        buffer += my_list[idx + idy]
    print(buffer / 3)

print()
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for idx in range(len(low_prices)):
    volatility.append(high_prices[idx] - low_prices[idx])

for value in volatility:
    print(value)
