# -*- coding: utf-8 -*-

import heapq

data = [
    (12.23, 'player1'),
    (12.31, 'player2'),
    (11.57, 'player3'),
    (12.04, 'player4'),
    (12.22, 'player5'),
    (11.92, 'player6')
]

h = []
for score in data:
    heapq.heappush(h, score)

for i in range(3):
    print(heapq.heappop(h))

print(len(h))
