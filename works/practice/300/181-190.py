# -*- coding: utf-8 -*-

listData = [["101", "102"], ["201", "202"], ["301", "302"]]
print(listData)

listData = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
print(listData)

stock = {"시가": [100, 200, 300], "종가": [80, 210, 330]}
print(stock)

stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}
print(stock)

apart = [[101, 102], [201, 202], [301, 302]]
for floor in apart:
    for house in floor:
        print(house, "호")

print()
for idx in range(len(apart) - 1, -1, -1):
    for house in apart[idx]:
        print(house, "호")

print()
for row in apart[::-1]:
    for col in row:
        print(col, "호")

print()
for row in apart[::-1]:
    for col in row[::-1]:
        print(col, "호")

print()
for floor in apart:
    for house in floor:
        print(house, "호")
        print("-----")

print()
for floor in apart:
    for house in floor:
        print(house, "호")
    print("-----")

print()
for floor in apart:
    for house in floor:
        print(house, "호")
print("-----")
