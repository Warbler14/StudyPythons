# for
print('----------------------------------------------------')
animalList = ['cat', 'dog', 'penguin', 'horse', 'tiger', 'bear']
for name in animalList:
    print(name)

print('----------------------------------------------------')
snackList = ['cup cake', 'doughnut', 'eclair', 'frozen yogurt', 'ginger bread', '...']

for idx, name in enumerate(snackList):
    print(idx, name)

print('----------------------------------------------------')
jewelList = ['ruby', 'emerald', 'sapphire', 'topaz', 'amethyst', 'diamond']

for idx, name in enumerate(jewelList):
    print(idx, jewelList[idx])

print('----------------------------------------------------')
hap = 0
for x in range(1, 11):
    hap = hap + x

print(hap)

print('----------------------------------------------------')
for x in range(2, 9):
    for y in range(2, 10):
        print(x, '*', y, '=', x*y)
    print

print('----------------------------------------------------')

