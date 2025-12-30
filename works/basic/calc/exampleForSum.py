total = 0
for i in range(1, 101):
    total += i
print(total)

i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(total)

# 파이썬 내장 함수
print(sum(range(1, 101)))

# 리스트 컴프리센션
print(sum([i for i in range(1, 101)]))

# 제너레이터 표현식 (메모리 효율)
print(sum(i for i in range(1, 101)))

# 수학 공식 (가우스 공식) 1부터 n까지의 합 = n × (n + 1) // 2
n = 100
print(n * (n + 1) // 2)

# 재귀 함수 (권장 X, 학습용)
def add(n):
    if n == 0:
        return 0
    return n + add(n - 1)

print(add(100))

# functools.reduce
#from functools import reduce
#print(reduce(lambda a, b: a + b, range(1, 101)))

# itertools.accumulate
#from itertools import accumulate
#print(list(accumulate(range(1, 101)))[-1])

#NumPy 사용 (과한 방법)
#import numpy as np
#print(np.sum(np.arange(1, 101)))

# map 사용
print(sum(map(int, range(1, 101))))

# 재귀 + 삼항 연산자
f = lambda n: 0 if n == 0 else n + f(n - 1)
print(f(100))

# eval (절대 권장 X)
#print(eval("+".join(map(str, range(1, 101)))))

# 비트 연산(?) (의미 없음, 이론용)
#print((100 * 101) >> 1)