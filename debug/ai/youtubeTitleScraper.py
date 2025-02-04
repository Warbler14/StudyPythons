from urllib.parse import quote
import requests
import re
import json
from bs4 import BeautifulSoup


def get_youtube_titles(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("페이지 요청 실패:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # JavaScript 안의 ytInitialData JSON 데이터 찾기
    scripts = soup.find_all("script")
    yt_data = None
    for script in scripts:
        if "var ytInitialData" in script.text:
            json_text = re.search(r"var ytInitialData = ({.*?});", script.text)
            if json_text:
                yt_data = json.loads(json_text.group(1))
            break

    if not yt_data:
        print("YouTube 데이터 추출 실패")
        return []

    # 영상 제목 추출
    video_titles = []
    try:
        contents = yt_data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]
        videos = contents["itemSectionRenderer"]["contents"]

        for video in videos:
            if "videoRenderer" in video:
                title = video["videoRenderer"]["title"]["runs"][0]["text"]
                video_titles.append(title)

    except KeyError:
        print("YouTube 페이지 구조가 변경되었거나, 크롤링이 차단되었습니다.")

    return video_titles


search_query = input("search query: ")

if len(search_query) == 0:
    print("search_query is empty")
    exit()

print("search_query : " + search_query)
encoded_search_query = quote(search_query)
print("encoded_search_query : " + encoded_search_query)

youtube_url = "https://www.youtube.com/results?search_query=" + encoded_search_query
titles = get_youtube_titles(youtube_url)

for idx, title in enumerate(titles, 1):
    print(f"{idx}. {title}")
