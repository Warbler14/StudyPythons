from urllib.request import urlopen
from bs4 import BeautifulSoup

import os.path


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

def fetch_from_urls(url_list, save_directory, _scoop ):
    for url in url_list:
        save_path = save_directory + to_file_name(url)
        if os.path.isfile(save_path):
            print(save_path + " found, nothing to do.")
        else:
            print("start fetch " + url + " and save : " + save_path)
            soup = fetch(url)
            element = _scoop(soup)
            download(save_path, element.text.encode())

def scoop(soup):
    return soup.find('td', {"class": "scrtext"})


base_directory = "/Users/kook/script/"
urls = [
    "https://imsdb.com/scripts/Star-Wars-Return-of-the-Jedi.html",
    "https://imsdb.com/scripts/Sleepless-in-Seattle.html"]

fetch_from_urls(urls, base_directory, scoop)
