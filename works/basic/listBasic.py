# -*- coding: utf-8 -*-
# 테스트 2021-12-11

print('----- index -----')
myList = [1, 2, 3]
print(myList)
print(myList[0], myList[1], myList[2])
print(myList[-1])
myList = [1, 2, 3, ['a', 'b', 'c']]
print(myList)
print(myList[3][0], myList[3][1], myList[3][2])
myList = [1, 2, ['a', 'b', ['life', 'is', 'good']]]
print(myList[2][2][0], myList[2][2][1], myList[2][2][2])

print('----- slice -----')
myList = [0, 1, 2, 3, 4, 5]
print(myList[0:2])
print(myList[2:])
myList = [0, 1, ['life', 'is', 'good'], 3]
print(myList[2][:])

print('----- mix -----')
myList1 = [0, 1, 2]
myList2 = [3, 4, 5]
print(myList1 + myList2)
print(myList1 * 2)
print(len(myList2), myList2.clear(), myList2)

print('----- edit -----')
myList = [0, 0, 0]
myList[1] = 1
myList[2] = 2
print(myList)
del myList[1]
print(myList)

print('----- function -----')
myList = [0, 1, 2, 3, 4, 5]
print(myList)
myList.append(6)
print(myList)
myList.append([7, 8])
print(myList)

myList = [5, 4, 3, 2, 1, 0]
myList.sort()
print(myList)
myList.reverse()
print(myList)

myList.insert(0, 6)
print(myList)
myList.remove(3)
print(myList)

value = myList.pop(3)
print('list : ', myList, ', pop value : ', value)
myList = [0, 0, 0, 1, 1, 2]
print(myList.count(0), myList.count(1), myList.count(2), myList.count(3))

myList = [0, 0, 0, 1, 1, 2]
myList.extend([3, 3])
print(myList)

print('----- conditional statement -----')
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print('walk')

if 'money' in pocket:
    print('take taxi')
elif 'bus_card' in pocket:
    print('take bus')
else:
    print('walk')

goods = 'pencil'
item = 'money'
note = 'buy' if item in pocket else 'borrow'
print(note, goods)

print('----- iteration -----')
coinBag = [500, 500, 10, 100, 500, 50, 10, 100, 100]
coinList = []

'''
list 에서 중복되지 않고 정렬된 값을 더 쉽게 가져올 수 없는가. ???
'''
sortedCoinList = list(set(coinBag))
sortedCoinList.sort()

idx = 0
while idx < len(coinBag):
    coin = coinBag[idx]

    if len(coinList) == 0:
        coinList.append([coin])
    else:
        x = 0
        found = False
        for box in coinList:
            if isinstance(box, list):
                if coinList[x][0] == coin:
                    found = True
                    break
                x = x + 1

        if found:
            coinList[x].append(coin)
        else:
            coinList.append([coin])

    idx = idx + 1

print(coinList)

coin500 = [coin for coin in coinBag if coin == 500]
print(coin500)