
from random import randint, random, randrange
from random import sample

# print(random())         # 0.0 ~ 1.0 미만의 임의의 값
# print(random() * 10)    # 0.0 ~ 10.0 미만의 임의의 값
# print(int(random() * 10))
# print(int(random() * 10))

print('------------ random() - 50 --------------')
randomResultList = []
for x in range(10):
    num = int(random() * 50) + 1
    randomResultList.append(num)

print(randomResultList)
print('------------ random() - 50 --------------')

print('------------ randrange() - 1 ~ 50 --------------')
randrangeResultList = []
for x in range(10):
    num = randrange(1, 50)
    randrangeResultList.append(num)

print(randrangeResultList)
print('------------ randrange() - 1 ~ 50 --------------')

print('------------ randint() - 1 ~ 50 --------------')
randintResultList = []
for x in range(10):
    num = randint(1, 50)
    randintResultList.append(num)

print(randintResultList)
print('------------ randint() - 1 ~ 50 --------------')

sampleList = [1, 2, 3, 4, 5]
print(sample(sampleList, 2))
