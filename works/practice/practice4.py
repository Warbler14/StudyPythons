
from random import randint, random, randrange, sample

# print(random())         # 0.0 ~ 1.0 미만의 임의의 값
# print(random() * 10)    # 0.0 ~ 10.0 미만의 임의의 값
# print(int(random() * 10))
# print(int(random() * 10))


def test_random(limit_val):
    result_list = []
    for x in range(10):
        num = int(random() * limit_val) + 1
        result_list.append(num)

    print(result_list)


def test_randrange(limit_val):
    result_list = []
    for x in range(10):
        num = randrange(1, limit_val)
        result_list.append(num)

    print(result_list)


def test_randint(limit_val):
    result_list = []
    for x in range(10):
        num = randint(1, limit_val)
        result_list.append(num)

    print(result_list)


limit = 3

print('------------ random() --------------')
test_random(limit)

print('------------ randrange() --------------')
test_randrange(limit)

print('------------ randint() --------------')
test_randint(limit)

print('------------ sample() --------------')
sampleList = [1, 2, 3, 4, 5]
print(sample(sampleList, 2))
