import requests
from bs4 import BeautifulSoup
import json


def make_url(url_address_head, object_file_name, object_extension):
    return url_address_head + object_file_name + object_extension

session = requests.Session()

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
            AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
			"Accept":"text/html,application/xhtml+xml,application/xml;\
			q=0.9,imgwebp,*/*;q=0.8"}

url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"

req = session.get(url, headers=header)
bs0bj = BeautifulSoup(req.text, "html.parser")
print(bs0bj.find("table", {"class": "table-striped"}).get_text)



