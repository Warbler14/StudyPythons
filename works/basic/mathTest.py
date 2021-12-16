from math import floor
from math import ceil
from math import sqrt
from decimal import *

print(1+1)
print(3-2)
print(5*2)
print(6/2)          # 3.0s

print(2 ** 3)       # 8
print(5 % 3)        # 2
print(5 // 3)       # 1

print(abs(-5))      # 5
print(pow(4, 2))    # 16
print(max(5, 10))   # 10
print(min(5, 10))   # 5
print(round(3.14))  # 3
print(round(4.5))   # 4

print(floor(4.99))  # 4
print(ceil(3.14))   # 4
print(sqrt(16))     # 4.0

# ------------------------------------------------------------------------------------------------------
h = 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
print(h)

a = 4 + 5j
print(a)            # (4+5j)
print(a.real)       # 4.0
print(a.imag)       # 5.0

A = Decimal(1234)
print(A)            # 1234
A = Decimal('1234.5678')
print(A)            # 1234.5678

