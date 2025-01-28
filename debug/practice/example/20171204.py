# -*- coding: utf-8 -*-
# 테스트 2017-12-04


newFile = open("NewFile.txt", "w")

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    newFile.write(data)

newFile.close()

# ================================================

readNewFile = open("NewFile.txt", "r")

while True:
    line = readNewFile.readline()
    if not line:
        break
    print(line)

readNewFile.close()

# ================================================

readNewFile = open("NewFile.txt", "r")

lines = readNewFile.readlines()
for line in lines:
    print(line)

readNewFile.close()

# ================================================

addNewFile = open("NewFile.txt", "a")
for idx in range(11, 20):
    data = "%d번째 줄입니다.\n" % idx
    addNewFile.write(data)
addNewFile.close()

# ================================================

readNewFile = open("NewFile.txt", "r")

lines = readNewFile.readlines()
for line in lines:
    print(line)

readNewFile.close()

