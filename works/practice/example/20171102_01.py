# -*- coding: utf-8 -*-
# 테스트 2017-11-02, 2021-11-25
import sys

print('Hello Python')
print('Hello "Python"')
print('Hello', 'Python')
print('Hello', "Python")
print('Hello' + "Python")
print()

print('I like Python.\
I like C++')

print("""I like Python.
I like C++""")

print('''I like Python.
I like C++''')

end = ' '
print('Hello',  end)

file = sys.stderr
print('Hello Python', file)

print('My mother\'s house')
print('\', \", \\, \a. \t, \n')

i = 123
f = 3.14
s = 'Hello'
print('i: %d, f: %f, s: %s' % (i, f, s))
print('i: %9d, f: %5.2f, s: %7s' % (i, f, s))
print('i: %09d, f: %05.2f, s: %7s' % (i, f, s))
print('i: {}, f: {}, s: {}' .format(i, f, s))
print('f: {1}, i: {0}, s: {2}' .format(i, f, s))
print('f: {ff}, i: {ii}, s: {ss}' .format(ii=i, ff=f, ss=s))

a = 'apple'
b = 'banana'
print('a is {0[a]}, b is {0[b]}'.format(locals()))
print('a is {a}, b is {b}'.format(**locals()))

print('Hello Python!'.center(20))
print('Hello Python!'.rjust(20))
print('Hello Python!'.ljust(20))
print('Hello Python!'.zfill(20))
print('Hello Python!'.capitalize())
print('Hello Python!'.upper())
print('Hello Python!'.lower())

print(123); print(3.14)
print(True)
print("3 * 2 = ", 3 * 2)
print(list(range(1, 10)))
