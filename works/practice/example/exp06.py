# dic

dic = {'one': 'haha', 'two': 'hoho', 'three': 'hihi'}
print(dic['one'])

# add 'four' : 'kiki'
dic['four'] = 'kiki'
print(dic)
dic['one'] = 1
print(dic)

print('two' in dic)

key = dic.keys()
print(key)

# print(key[0])

values = dic.values()
print(values)

# print(values[0])

items = dic.items()
print(items)
