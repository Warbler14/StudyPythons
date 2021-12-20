__author__ = 'insung'

def add(a, b):
    return a+b


print(add(1, 2))

a, b = 1, 2
c, d = 3, 4
x = y = z = 0
e = 3.5; f = 5.6
print(a,   b,   c,   d,   e,   f)

a = 2
a *= 2+3
print(a)

a = eval('a + a + 10')
print(a)

a = 5
exec('a = a + 4')
print(a)

