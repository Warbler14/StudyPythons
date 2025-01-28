
word = 'Hello World!'
print(word[0])
print(word[1])
print(word[2])
print(word[-1])
print(word[1:5])
print(word[1:])
print(word[:5])
print(word[:])

str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(str1[::2])
print(str1[::-1])

print('Hello ' * 3)
print('a' + str1[1::1])
print('(' + str1[0:len(str1)] + ')')

print('M' in str1)
print('m' in str1)

number_list = [1, 2, 3]
print(number_list)
number_list.append(4)
print(number_list)
print(number_list[0])
print(number_list[0:len(number_list)])
print(number_list[len(number_list) - 1])
buffer = number_list[len(number_list) / 2]
del number_list[len(number_list) / 2]
print(number_list)
number_list.reverse()
print(number_list)
number_list.append(buffer)
number_list.sort()
print(number_list)
