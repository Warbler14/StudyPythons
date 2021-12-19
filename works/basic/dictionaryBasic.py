# -*- coding: utf-8 -*-
import copy

dic1 = {'name': 'robin', 'phone': '01011112222', 'birth': '0111'}
print(dic1)             # {'name': 'robin', 'phone': '01011112222', 'birth': '0111'}

dic1['job'] = 'programmer'
print(dic1)             # {'name': 'robin', 'phone': '01011112222', 'birth': '0111', 'job': 'programmer'}
print(dic1.keys())      # dict_keys(['name', 'phone', 'birth', 'job'])
print('name' in dic1)   # True


for key in dic1.keys():
    print("key : " + key + ", value : " + dic1[key])

print(dic1.items())     # dict_items([('name', 'robin'), ('phone', '01011112222'), ('birth', '0111'), ('job', 'programmer')])

dic2 = dic1
print(id(dic1), id(dic2))           # 4469544384 4469544384
dic2['hobby'] = 'coding'
print(id(dic1), id(dic2))           # 4469544384 4469544384
dic2 = copy.deepcopy(dic1)
print(id(dic1), id(dic2))           # 4352370112 4353951872
dic2['hobby'] = 'reading'

dic3 = {}
print(dic3)                         # {}
dic3[1] = 1000
print(dic3)                         # {1: 1000}
dic3[2] = 2000
del dic3[1]
print(dic3)                         # {2: 2000}
print(dic3[2], " ", dic3.get(2))    # 2000   2000

dic3.clear()
print(dic3)                         # {}
print(dic3.get(2, 'default'))       # default
