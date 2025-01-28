# -*- coding: utf-8 -*-

ticker = "btc_krw"
print(ticker.upper())

ticker = "BTC_KRW"
print(ticker.lower())

string = 'hello'
print(string[0].upper() + string[1:])
print(string.capitalize())

file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

print(file_name.endswith(('xlsx', 'xls')))

file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

a = "hello world"
print(a.split())

ticker = "btc_krw"
print(ticker.split('_'))

date = "2020-05-01"
print(date.split('-'))

data = "  039490     "
print(data.rsplit())
