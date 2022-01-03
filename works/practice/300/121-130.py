# -*- coding: utf-8 -*-
import requests


# ch = input()
# if ch[0].upper() == ch[0]:
#     print(ch[0].lower())
# else:
#     print(ch[0].upper())

# score = int(input("score: "))
# grade = None
# if score > 80:
#     grade = 'A'
# elif score > 60:
#     grade = 'B'
# elif score > 40:
#     grade = 'C'
# elif score > 20:
#     grade = 'D'
# else:
#     grade = 'E'
# print("grade is " + grade)

# cash_price = {"dollar": 1167, "yen": 1.096, "eur": 1268, "cny": 171}
# # data = input("입력: ").split(" ")
# # won = float(data[0]) * cash_price[data[1]]
# # print(won, "원")
# num, currency = input("입력: ").split()
# print(float(num) * cash_price[currency], "원")

# numberList = []
# for n in range(1, 4):
#     number = int(input("input number" + str(n) + ": "))
#     numberList.append(number)
# print(max(numberList))

# telecom = {"SKT": ["011"], "KT": ["016"], "LGU": ["019"], "알수없음": ["010"]}
# phone_number = input("휴대전화 번호 입력: ")
# first_block = phone_number[:3]
#
# telecom_number = telecom.values()
# for key in telecom:
#     company = telecom[key]
#     if first_block in company:
#         print("당신은 {} 사용자입니다.".format(key))
#         break

# postal_code = input("우편번호: ")
# if postal_code[:2] == "01":
#     third = int(postal_code[2])
#     if third < 0:
#         None
#     elif third < 3:
#         print("강북구")
#     elif third < 6:
#         print("도봉구")
#     else:
#         print("노원구")

# personal_code = input("주민등록번호: ")
# sex = personal_code[7]
# if sex in ["1", "3"]:
#     print("남자")
# if sex in ["2", "4"]:
#     print("여자")

# personal_code = input("주민등록번호: ")
# code = personal_code.split("-")[1]
# print(code[1:3])
# codeNumber = int(code[1:3])
# if codeNumber < 9:
#     print("서울 입니다.")
# else:
#     print("서울이 아닙니다.")

# personal_code = input("주민등록번호: ").replace("-", "")
# if len(personal_code) == 13:
#     result = int(personal_code[0]) * 2 + \
#              + int(personal_code[1]) * 3 + \
#              + int(personal_code[2]) * 4 + \
#              + int(personal_code[3]) * 5 + \
#              + int(personal_code[4]) * 6 + \
#              + int(personal_code[5]) * 7 + \
#              + int(personal_code[6]) * 8 + \
#              + int(personal_code[7]) * 9 + \
#              + int(personal_code[8]) * 2 + \
#              + int(personal_code[9]) * 3 + \
#              + int(personal_code[10]) * 4 + \
#              + int(personal_code[11]) * 5
#     result = 11 - (result % 11)
#     if int(personal_code[-1]) != result:
#         print("유효하지 않은 주민등록번호입니다.")
#     else:
#         print("유효한 주민등록번호입니다.")

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

opening_price = float(btc['opening_price'])
max_price = float(btc['max_price'])
gap = max_price - float(btc['min_price'])
print(opening_price, max_price, gap)

if (opening_price + gap) > max_price:
    print("상승장")
else:
    print("하락장")
