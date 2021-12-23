# -*- coding: utf-8 -*-

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(scores)

a, b, *valid_score = scores
print(scores)

a, *valid_score, b = scores
print(valid_score)

temp = {}
print(type(temp))

ice_cream = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
print(ice_cream)

ice_cream['죠스바'] = 1200
ice_cream['월드콘'] = 1500
print(ice_cream)

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(ice['메로나'])

ice['메로나'] = 1300
print(ice['메로나'], ice.get('메로나'))

del ice['메로나']
print(ice.get('메로나'))

# ice['누가바']  # KeyError: '누가바'

