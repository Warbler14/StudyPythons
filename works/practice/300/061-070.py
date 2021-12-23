# -*- coding: utf-8 -*-

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = nums[::2]
print(odd_nums)

even_nums = nums[1::2]
print(even_nums)

nums = [1, 2, 3, 4, 5]
print(nums[::-1])

interest = ['Google', 'Apple', 'IBM']
print(interest[0], interest[2])

interest = ['Google', 'Apple', 'IBM', 'Intel', 'Microsoft']
print(' '.join(interest))

print('/'.join(interest))

print('\n'.join(interest))

string = 'Google/Apple/IBM'
interest = string.split('/')
print(interest)

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
data2 = sorted(data)
print(data, data2)
