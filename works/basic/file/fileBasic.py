# -*- coding: utf-8 -*-

filePath = "note.txt"
file = open(filePath, 'w')
for i in range(1, 11):
    file.write("%d\n" % i)
file.close()

file = open(filePath, 'r')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close()

file = open(filePath, 'r')
lines = file.readlines()
for line in lines:
    line = line.split()
    print(line)
file.close()

file = open(filePath, 'a')
for i in range(11, 21):
    file.write("%d\n" % i)
file.close()

with open(filePath, 'a') as file:
    for i in range(21, 31):
        file.write("%d\n" % i)
