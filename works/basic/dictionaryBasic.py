# -*- coding: utf-8 -*-
import copy

# 전체 출력
dic1 = {'name': 'robin', 'phone': '01011112222', 'birth': '0111'}

# 값 추가 와 목록 출력
print('before : ', dic1)             # {'name': 'robin', 'phone': '01011112222', 'birth': '0111'}
dic1['job'] = 'programmer'
print('after add element : ', dic1)             # {'name': 'robin', 'phone': '01011112222', 'birth': '0111', 'job': 'programmer'}

print("'name' in dictionary : ", end="")
print('name' in dic1)   # True

print('dictionary keys  :', dic1.keys())      # dict_keys(['name', 'phone', 'birth', 'job'])
for key in dic1.keys():
    print("key : " + key + ", value : " + dic1[key])

print("items : ", dic1.items())     # dict_items([('name', 'robin'), ('phone', '01011112222'), ('birth', '0111'), ('job', 'programmer')])

print("--------------------------------------------")

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


language = {}
language['java'] = 'terran'
language['javascript'] = 'zerg'
language['python'] = 'protoss'

for key in language.keys():
    print(key, '=', language[key])


dic4 = {'name1': 'tom'}
dic5 = {'name2': 'max'}
dic4.update(dic5)
print(dic4)
print(dic5)


