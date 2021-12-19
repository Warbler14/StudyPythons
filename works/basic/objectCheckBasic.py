# -*- coding: utf-8 -*-

L1 = [1, 2, 3]
L2 = [1, 2, 3]

print(L1 is L2)     # False
print(L1 == L2)     # True

T1 = (1, 2, 3)
T2 = (1, 2, 3)

print(T1 is T2)     # True
print(T1 == T2)     # True

D1 = {"a": "a", "b": "b"}
D2 = {"a": "a", "b": "b"}

print(D1 is D2)     # False
print(D1 == D2)     # True
