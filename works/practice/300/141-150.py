# -*- coding: utf-8 -*-

리스트 = [100, 200, 300]
부가세 = 10
for item in 리스트:
    print(item + 부가세)

리스트 = ["김밥", "라면", "튀김"]
message = "오늘의 메뉴:"
for menu in 리스트:
    print(message, menu)

리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for stock in 리스트:
    print(len(stock))

리스트 = ['dog', 'cat', 'parrot']
for animal in 리스트:
    print(animal, len(animal))

리스트 = ['dog', 'cat', 'parrot']
for animal in 리스트:
    print(animal[0])

리스트 = [1, 2, 3]
number = 3
for item in 리스트:
    print(number, 'x', item)

리스트 = [1, 2, 3]
number = 3
for item in 리스트:
    print(number, 'x', item, '=', number * item)

리스트 = ["가", "나", "다", "라"]
for idx in range(1, 4):
    print(리스트[idx])
for 변수 in 리스트[1:]:
    print(변수)

print()

리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[0::2]:
    print(변수)

print()

리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[::-1]:
    print(변수)
