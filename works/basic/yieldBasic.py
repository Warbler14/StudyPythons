# -*- coding: utf-8 -*-

import time

# Python의 내장 함수 id()는 객체의 "고유 식별자"를 반환합니다.
# 이 고유 식별자는 객체가 메모리에서 저장된 위치(메모리 주소)와 밀접하게 관련되어 있습니다.
# CPython 구현에서, id() 함수는 객체의 메모리 주소를 정수로 반환합니다.
# 객체 비교: id()를 사용하면 두 객체가 실제로 동일한 객체인지 확인할 수 있습니다.
# 객체 추적: 메모리 주소나 객체 참조를 추적할 때 사용합니다.
# Immutable 객체: 불변 객체(예: 숫자, 문자열)는 동일 값에 대해 동일한 ID를 공유하는 경우가 많습니다.
# Python에서 id() 함수는 빌트인으로 제공되므로 C로 구현되어 있습니다. Python 코드로 간단히 표현하면 아래와 같이 생각할 수 있습니다:
# def id(obj):
#     return obj.__memory_address__
# id()는 Python의 구현에 따라 동작이 달라질 수 있습니다
# CPython에서는 메모리 주소를 반환하지만, 다른 Python 구현(PyPy, Jython 등)에서는 다른
# id()로 반환된 값은 객체가 메모리에서 해제되면 재사용될 수 있습니다.
# 참고 : https://wikidocs.net/22802

def return_abc():
    alphabets = []
    for ch in "ABC":
        # time.sleep(1)
        alphabets.append(ch)
    return alphabets

def yield_abc():
    for ch in "ABC":
        # time.sleep(1)
        yield ch

def yield_from_abc():
    yield from ["A", "B", "C"]

def print_array(array):
    for ch in array:
        print(ch, end=" ")
    print()
def test_times(_funciton, count):
    for i in range(count):
        print(id(_funciton()))
    print("---")
    for i in range(count):
        buffer = _funciton()
        print(id(buffer))

print("------ return print -----")
return_abc_obj_1 = return_abc()
return_abc_obj_2 = return_abc()
print(return_abc_obj_1, id(return_abc_obj_1))
print(return_abc_obj_2, id(return_abc_obj_2))
test_times(return_abc, 5)

print("------ yield print -----")

print(yield_abc())
print(yield_abc())
yield_abc_obj_1 = yield_abc()
yield_abc_obj_2 = yield_abc()
print(yield_abc_obj_1, id(yield_abc_obj_1))
print(yield_abc_obj_2, id(yield_abc_obj_2))
test_times(yield_abc, 5)
print_array(yield_abc())

print("------ yield from print -----")

print(yield_from_abc())
print(yield_from_abc())
yield_abc_obj_1 = yield_from_abc()
yield_abc_obj_2 = yield_from_abc()
print(yield_abc_obj_1, id(yield_abc_obj_1))
print(yield_abc_obj_2, id(yield_abc_obj_2))
test_times(yield_from_abc, 5)
print_array(yield_from_abc())

# 메모리 효율성: 모든 값을 미리 메모리에 저장하지 않고, 필요할 때마다 생성합니다.
# 게으른 계산(lazy evaluation): 값을 바로 생성하지 않고 필요할 때 생성합니다.
# 제너레이터 객체는 이터러블로 사용할 수 있기 때문에 for문에서도 활용 가능합니다.
# 제너레이터 표현식은 ( )로 감싸져 있으므로, 실행 결과는 값들이 바로 계산되는 것이 아니라
# 필요할 때 하나씩 생성될 제너레이터 객체가 됩니다.
print("------ yield Generator Comprehension print -----")
abc = (ch for ch in "ABC")
print(abc) #<generator object <genexpr> at 0x109bfeeb0>
print_array(abc)