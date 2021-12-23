# -*- coding: utf-8 -*-

my_variable = ()

movie_rank = ('Doctor Strange', 'Spider Man', 'Iron Man')

number_tuple = (1, )
print(type(number_tuple))

t = (1, 2, 3)
# t[0] = '0'  # TypeError: 'tuple' object does not support item assignment

t = 1, 2, 3, 4
print(type(t))

t = ('a', 'b', 'c')
t2 = ('A', t[1], t[2])
print(t, t2)

interest = ('Google', 'Apple', 'IBM')
interest_list = list(interest)
print(interest_list)

interest = ['Google', 'Apple', 'IBM']
print(tuple(interest))

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

data = tuple(range(2, 100, 2))
print(data)
