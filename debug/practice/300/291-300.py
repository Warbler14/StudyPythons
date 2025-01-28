# -*- coding: utf-8 -*-
import csv

print("-=-291-=-")
fileName = "매수종목1.txt"
file = open(fileName, mode="wt", encoding="utf-8")
file.write("005930\n")
file.write("005380\n")
file.write("035420")
file.close()

print("-=-292-=-")
fileName = "매수종목2.txt"
file = open(fileName, mode="wt", encoding="utf-8")
file.write("005930 삼성전자\n")
file.write("005380 현대차\n")
file.write("035420 NAVER")
file.close()

print("-=-293-=-")
fileName = "매수종목.csv"
file = open(fileName, mode="wt", encoding="cp949", newline='')
writer = csv.writer(file)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
file.close()

print("-=-294-=-")
fileName = "매수종목1.txt"
file = open(fileName, mode="r", encoding="utf-8")
dataList = []
while True:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    dataList.append(line)
file.close()
print(dataList)

print("-=-295-=-")
fileName = "매수종목2.txt"
file = open(fileName, mode="r", encoding="utf-8")
dataDict = {}
lines = file.readlines()
file.close()

for line in lines:
    key, value = line.strip().split()
    dataDict[key] = value

print(dataDict)

print("-=-296-=-")
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

print("-=-297-=-")
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)

print(new_per)


print("-=-298-=-")
try:
    v = 10 / 0
except ZeroDivisionError:
    print('ZeroDivisionError')

print("-=-299-=-")
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

print("-=-300-=-")
per = ["10.31", "", "8.00"]

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    else:
        pass
    finally:
        print(v)
