# -*- coding: utf-8 -*-

# message = input()
# print(message * 2)

# numVar = int(input('숫자를 입력하세요: '))
# print(numVar + 10)

# numVar = int(input('input number : '))
# if numVar % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# limit = 255
# numVar = int(input('input number : '))
# numVarAdd20 = numVar + 20
# if numVarAdd20 > limit:
#     print(limit)
# else:
#     print(numVarAdd20)

# limitUnder = 0
# limitTop = 255
# numVar = int(input('input number : '))
# numVarSub20 = numVar - 20
# if numVarSub20 < limitUnder:
#     print(limitUnder)
# elif numVarSub20 > limitTop:
#     print(limitTop)
# else:
#     print(numVarSub20)

# userTime = input('현재 시간 : ').split(":")
# minute = int(userTime[-1])
# if minute == 0:
#     print('정각 입니다.')
# else:
#     print('정각이 아닙니다.')

# fruit = ["사과", "포도", "홍시"]
# item = input('좋아하는 과일은? ')
# if item in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# item = input('종목명? ')
# if item in warn_investment_list:
#     print("투자 경고 종목입니다")
# else:
#     print("투자 경고 종목이 아닙니다.")

# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# item = input('제가좋아하는계절은 : ')
# if item in fruit:
#     print("정답입니다")
# else:
#     print("오답입니다")

fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
item = input('좋아하는과일은 : ')
if item in fruit.values():
    print("정답입니다")
else:
    print("오답입니다")
