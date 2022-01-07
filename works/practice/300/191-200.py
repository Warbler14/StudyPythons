# -*- coding: utf-8 -*-

data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
commission = 1.00014

for row in data:
    for price in row:
        print(price * commission)

print()
for row in data:
    for price in row:
        print(price * commission)
    print("----")

print()
result = []
for row in data:
    for price in row:
        result.append(price * commission)
print(result)

print()
result = []
for row in data:
    volume = []
    for price in row:
        volume.append(price * commission)
    result.append(volume)
print(result)

print()
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
    print(row[3])

print()
for row in ohlc[1:]:
    if row[3] > 150:
        print(row[3])

print()
for row in ohlc[1:]:
    if row[3] >= row[0]:
        print(row[3])

print()
volatility = []
for row in ohlc[1:]:
    volatility.append(row[1] - row[2])
print(volatility)

print()
buffer = []
for row in ohlc[1:]:
    if row[0] < row[3]:
        print(row[1] - row[2])

print()
result = 0
for row in ohlc[1:]:
    value = row[3] - row[0]
    result += value
print(result)
