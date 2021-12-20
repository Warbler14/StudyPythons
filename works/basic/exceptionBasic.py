# -*- coding: utf-8 -*-

print('--- test ZeroDivisionError ---')
number = 100
filePath = "./file/text.txt"
file = open(filePath, 'w')
try:
    for i in range(10, -10, -1):
        data = number / i
        print(number, '/', i, '=', data)
        file.write("%f\n" % data)

except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.', e)
finally:
    file.close()


print('--- test IndexError ---')
try:
    list1 = [1, 2]
    for x in range(0, 4):
        print(list1[x])
except IndexError as e:
    print('인덱싱 할 수 없습니다.', e)


try:
    f = open('empty.txt', 'r')
except FileNotFoundError as e:
    pass
    # print(e)
    # [Errno 2] No such file or directory: 'empty.txt'


class Bird:
    def fly(self):
        raise NotImplementedError

'''
class Eagle(Bird):
    pass


eagle = Eagle()
eagle.fly()
'''

print('--- test override ---')
class Eagle(Bird):
    def fly(self):
        print('very fast')


eagle = Eagle()
eagle.fly()


print('--- test raise Exception ---')
class MyError(Exception):
    def __str__(self):
        return 'not allowed'


def say_nick(nick):
    if nick == 'fool':
        raise MyError()
    print(nick)


try:
    say_nick('angel')
    say_nick('fool')
except MyError as e:
    print(e)
