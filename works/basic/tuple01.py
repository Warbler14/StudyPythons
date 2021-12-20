import sys
sys.path.append('/Users/kook/workspaces/pywork/StudyPython/works/common')
from util import *

fruit = {"orange": "a sweet, citrus fruit"
         , "apple": "good for making cider"
         , "lemon": "a sour, yellow citrus fruit"
         , "grape": "a small, sweet fruit growing in bunches"
         , "lime": "a sour, green citrus fruit"}

print(fruit)

print(fruit.keys())
print_line_x('~~~~~~~~')

ordered_keys = list(fruit.keys())
print(ordered_keys)
print_line_x('~~~~~~~~')

ordered_keys.sort()
print(ordered_keys)
print_line_x('~~~~~~~~')

ordered_keys = sorted(list(fruit.keys()))
print(ordered_keys)
print_line_x('~~~~~~~~')

for f in ordered_keys:
    print(f + " - " + fruit[f])
print_line_x('~~~~~~~~')

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])
print_line_x('~~~~~~~~')

for f in sorted(fruit):
    print(f + " - " + fruit[f])
print_line_x('~~~~~~~~')

fruit["tomato"] = "tomato"

for f in sorted(fruit):
    print(f + " - " + fruit[f])
print_line_x('~~~~~~~~')

t_fruit = tuple(fruit.items())
for snack in sorted(t_fruit):
    item, description = snack
    print(item + " = " + description)
print_line_x('~~~~~~~~')


scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items():
    print(subject, " ", str(score))
    
    
