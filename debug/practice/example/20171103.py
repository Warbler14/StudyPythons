# -*- coding: utf-8 -*-
# 테스트 2017-11-03
import random

randomNumber = random.randrange(1, 100)

print(randomNumber)

print('숫자 맞추기 1~100 (기회는 10번)\n')


tryCount = 10
checkCount = 1

while checkCount < tryCount:
    message = "[" + str(checkCount) + ":" + str(tryCount) + "] 숫자를 입력해주세요 : "
    inputNumber = int(input(message))
    
    if randomNumber == inputNumber:
        print('정답입니다. ' + str(checkCount) + '회')
        break
    elif randomNumber > inputNumber:
        print(str(inputNumber) + ' 보다 큰 값입니다.')
    else:
        print(str(inputNumber) + ' 보다 작은 값입니다.')

    checkCount = checkCount + 1

print('종료')

