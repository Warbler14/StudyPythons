# -*- coding: utf-8 -*-

complicated = [1, (1, 2, (3, 4))]
print(complicated)
print(complicated[1][2][0])

list01 = ['01', '02']
print(list01)
list01[1] = '_02'
print(list01)

str01 = 'pycharm community edition 5.0.3'
print(str01[:])
print(str01[::2])
print(str01[::-1])

for x in range(10):
    if x > 3:
        break
    print(x)

print('done')
2

e, f, g = 3.14, 2.16e-9, 3E220
print(e, f, g)
