from random import randint
from random import sample

start = 0
end = 30


for idx in range(0, 10):
    random_val = str(randint(start, end))
    print(random_val)

# print(random())         # 0.0 ~ 1.0 미만의 임의의 값
# print(random() * 10)    # 0.0 ~ 10.0 미만의 임의의 값
# print(int(random() * 10))
# print(int(random() * 10))

# print(int(random() * 10) + 1)   # 1 ~ 10 이하의 임의의 값
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)

# print(int(random() * 45) + 1)   # 1 ~ 45 이하의 임의의 값
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45))   #1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))   #1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))   #1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))   #1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))   #1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))   #1 ~ 45 이하의 임의의 값 생성


list = [1, 2, 3, 4, 5]
print(sample(list, 2))
