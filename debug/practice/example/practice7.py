printBuffer = []
a = 20
b = 20


def print_and_clear(print_buffer):
    print(print_buffer)
    print_buffer.clear()


if a < b:
    print(str(b) + " is bigger then " + str(a))
elif b > a:
    print(str(a) + " is bigger then " + str(b))
else:
    print(str(a) + " is equal " + str(b))


catList = ['cat', 'lion', 'tiger', 'panther', 'cheetah', 'leopard']

for cat in catList:
    print(cat)
print("=========================================")
for k, cat in enumerate(catList):
    print(str(k) + "~" + cat)

print("=========================================")
for n in range(10):
    printBuffer.append(str(n))

print_and_clear(printBuffer)
print("=========================================")
for n in range(1, 11):
    printBuffer.append(str(n))

print_and_clear(printBuffer)
print("=========================================")
for n in list(range(100, 111)):
    printBuffer.append(str(n))

print_and_clear(printBuffer)
print("=========================================")
sumResult = 0
for n in range(1, 11):
    sumResult += n
print(sumResult)
print("=========================================")
enumerateList = list(range(10))
for k, ele in enumerate(enumerateList):
    enumerateList[k] = ele + 10

print(enumerateList)
print("=========================================")
for x in range(1,11):
    if x < 8:
        continue
    print(x)
print("=========================================")
for x in range(1, 6):
    if x == 5:
        break
    print(x)
else:
    print('break not works')
print('done')
print("=========================================")
count = 1
while count < 11:
    print(count)
    count += 1
print("=========================================")
sumData = 0
count = 1
while count < 11:
    sumData += count
    count += 1
print(sumData)
print("=========================================")
x = 1
while x < 11:
    if x == 10:
        break
    x += 1
else:
    print('break not works')
print('done' + str(x))
