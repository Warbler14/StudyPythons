from urllib.request import urlopen
from bs4 import BeautifulSoup

# ----------------------------------------
# required
# ----------------------------------------
# pip install beautifulsoup4
# pip install lxml
# ----------------------------------------
def download(save_file_name, text):
    with open(save_file_name, "wb") as file:
        file.write(text)
        file.close()
    return True

def fetch(target_url):
    response = urlopen(target_url)
    content_type = response.getheader('Content-Type')
    encode_charset = str(content_type.rsplit('=', 1)[1])
    return BeautifulSoup(response, "lxml", from_encoding=encode_charset)

def to_file_name(target_url):
    data = target_url.rsplit('/', 1)[1]
    data = data.replace(".html", ".txt")
    return data

url = "https://imsdb.com/scripts/Star-Wars-Return-of-the-Jedi.html"
base_directory = "/Users/kook/script/"
save_path = base_directory + to_file_name(url)



bsObject = fetch(url)

element = bsObject.find('td', {"class":"scrtext"})

download(save_path, element.text.encode())
