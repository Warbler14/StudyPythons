# -*- coding: utf-8 -*-

# set 은 중복을 허용하지 않는다. 순서가 없다.

s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)

t1 = tuple(s1)
print(t1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('intersection ', s1 & s2)
print('intersection ', s1.intersection(s2))
print('union ', s1 | s2)
print('union ', s1.union(s2))
print('difference ', s1 - s2, s2 - s1)
print('difference ', s1.difference(s2), s2.difference(s1))

s3 = set([0])
print(s3)
s3.add(1)
print(s3)
s3.update([2, 3, 4])
print(s3)
s3.remove(0)
print(s3)
