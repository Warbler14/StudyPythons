# -*- coding: utf-8 -*-

# 리스트는 [] 튜플은 ()
# 튜플은 값을 바꿀 수 없다.

t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print(t5[1:])   # ('b', ('ab', 'cd'))
t6 = t2 + t3
print(t6)       # (1, 1, 2, 3)
print(t3 * 3)   # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(len(t5))  # 3

print('----- iteration -----')
marks = (90, 25, 67, 45, 80)

total = 0
for mark in marks:
    total = total + mark

print(total)

for mark in marks:
    total = 0
    for i in range(1, mark):
        total = total + i
    print(mark, ' : ', total)
