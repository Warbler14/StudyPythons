# -*- coding: utf-8 -*-

import time


def return_abc():
    alphabets = []
    for ch in "ABC":
        time.sleep(1)
        alphabets.append(ch)
    return alphabets


def yield_abc():
    for ch in "ABC":
        time.sleep(1)
        yield ch


def yield_from_abc():
    yield from ["A", "B", "C"]


print("------ return print -----")
return_abc_obj_1 = return_abc()
return_abc_obj_2 = return_abc()
print(return_abc_obj_1, id(return_abc_obj_1))
print(return_abc_obj_2, id(return_abc_obj_2))
for ch in return_abc():
    print(ch)

print("------ yield print -----")

print(yield_abc())
print(yield_abc())
yield_abc_obj_1 = yield_abc()
yield_abc_obj_2 = yield_abc()
print(yield_abc_obj_1, id(yield_abc_obj_1))
print(yield_abc_obj_2, id(yield_abc_obj_2))
for ch in yield_abc():
    print(ch)

print("------ yield from print -----")

print(yield_from_abc())
print(yield_from_abc())
yield_abc_obj_1 = yield_from_abc()
yield_abc_obj_2 = yield_from_abc()
print(yield_abc_obj_1, id(yield_abc_obj_1))
print(yield_abc_obj_2, id(yield_abc_obj_2))
for ch in yield_from_abc():
    print(ch)


print("------ yield Generator Comprehension print -----")
abc = (ch for ch in "ABC")
print(abc)

for ch in abc:
    print(ch)