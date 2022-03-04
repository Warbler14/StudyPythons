# -*- coding: utf-8 -*-

import time


def return_abc():
    alpabets = []
    for ch in "ABC":
        time.sleep(1)
        alpabets.append(ch)
    return alpabets


def yield_abc():
    for ch in "ABC":
        time.sleep(1)
        yield ch


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
