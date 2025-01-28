# -*- coding: utf-8 -*-
# 테스트 2017-11-01

animal = 'pig'
print(animal)

family = ['mother', 'father', 'son', 'daughter']

print(len(family))
print(family[0])

family.remove('son')
print(len(family))

print('직각삼각형 그리기\n')
d = float(input('변의 길이 : '))

for i in range(int(d) + 1):
    print('* ' * i)

area = float((d ** 2) / 2)
print('넓이 : %s' % area)