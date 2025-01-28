__author__ = 'insung'

# ---- test print ----
print('test python');

a = 3

# ---- test if ----
if a > 1:
    print("a is greater than 1")

# ---- test for ----
for a in [1, 2, 3]:
    print(a)

    if a > 1:
        print(" a is greater than 1")

print("start for range 0 - 10")
for i in range(0, 10):
    print(i)
print("end for")


# ---- test while ----
i = 0
while i < 3:
    i += 1
    print(i)

# ---- test function ----
def sum1(v1, v2):
    return v1+v2

print(sum1(100, 99))

# ---- test complex ----
r = 1 + 2j

print(r.real, r.imag, r.conjugate(), abs(r))

# ---- test ** ----
a = 3
b = 4
print(a ** b)

# ---- test ' " ----

print("print this ' ")
print("print this '' ")
print("print this \' ")


# ---- test recursion ----
print("<< test recursion >>")

def countdown(n):
    if n == 0:
        print("fin")
    else:
        print(n)
        countdown(n-1)

countdown(10)

# ---- test multiplication table ----
print("<< test multiplication table use while >>")
num1 = 2
while num1 <= 9:
    num2 = 1
    while num2 <= 9:
        print(num1, ' * ', num2, ' = ', num1*num2)
        num2 += 1
    num1 += 1

print("<< test multiplication table use for >>")

for num1 in range(2, 9):
    for num2 in range(1, 9):
        print(num1, ' * ', num2, ' = ', num1*num2)
