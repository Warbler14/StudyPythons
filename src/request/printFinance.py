from urllib.request import urlopen
from bs4 import BeautifulSoup

# pip install beautifulsoup4
# pip install lxml

code = '032500'

html = urlopen("https://finance.naver.com/item/main.nhn?code=" + code)
bsObject = BeautifulSoup(html, "lxml", from_encoding='utf-8')

no_today = bsObject.find('p', {"class":"no_today"})
blind = no_today.find('span', {"class":"blind"})
live_cost = blind.text

print(live_cost)
