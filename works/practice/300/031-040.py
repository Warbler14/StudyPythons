# -*- coding: utf-8 -*-

a = "3"
b = "4"
print(a + b)

print("HI" * 3)

print('-' * 80)

t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 4)

name1 = '보아뱀'
age1 = 10
name2 = '구렁이'
age2 = 12
print('이름: %s 나이: %d' % (name1, age1))
print('이름: %s 나이: %d' % (name2, age2))

print('이름: {} 나이: {}'.format(name1, age1))
print('이름: {name} 나이: {age}'.format(name=name2, age=age2))
print('이름: {0} 나이: {1}'.format('꽃뱀', 19))

name3 = 'anaconda'
template = f'이름: {name3} 나이: {100 + 1}'
print(template)

상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(',', '')))

분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

data = "   대한민국    "
print(data.strip())
