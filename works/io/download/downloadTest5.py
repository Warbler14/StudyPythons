from requests import get
import datetime
import calendar
import progressbar
import urllib.request

progress_bar = None


def get_time_arr(s_year, s_month, s_day, e_year, e_month, e_day):
    result_arr = []
    for cur_year in range(s_year, e_year+1):
        start_month = 1
        if cur_year == s_year:
            start_month = s_month

        end_month = 12 + 1
        if cur_year == e_year:
            end_month = e_month + 1

        for cur_month in range(start_month, end_month):
            max_day = calendar.monthrange(cur_year, cur_month)[1]

            rs_day = 1
            if cur_year == s_year and cur_month == s_month and s_day > 1:
                rs_day = s_day

            for cur_day in range(rs_day, max_day + 1):
                date = datetime.date(cur_year, cur_month, cur_day)
                if cur_year == e_year and cur_month == e_month and cur_day == e_day + 1:
                    break

                day_time = date.strftime("%Y%m%d")
                result_arr.append(day_time)

    return result_arr


def show_progress(block_num, block_size, total_size):
    global progress_bar
    if progress_bar is None:
        progress_bar = progressbar.ProgressBar(maxval=total_size)

    downloaded = block_num * block_size
    if downloaded < total_size:
        progress_bar.update(downloaded)
    else:
        progress_bar.finish()
        progress_bar = None


def sub_string(target, word):
    return target[target.rfind(word) + len(word): len(target)]

# http://podcastfile.imbc.gscdn.com/originaldata/nightletter/NIGHTLETTER_20200511.mp3
# http://podcastfile.imbc.gscdn.com/originaldata/starnight/STARNIGHT_20200511.mp3

fileKey = "STARNIGHT_"
savePathRoot = "/Users/kook/Pictures/radio/STARNIGHT/"
urlRoot = "http://podcastfile.imbc.gscdn.com/originaldata/starnight/"

startYear = 2020
startMonth = 5
startDay = 11
endYear = 2020
endMonth = 5
endDay = 14

resultArr = get_time_arr(startYear, startMonth, startDay, endYear, endMonth, endDay)

for idx in range(len(resultArr)):
    url_address = urlRoot + fileKey + resultArr[idx] + ".mp3"
    fileName = fileKey + sub_string(url_address, fileKey)
    savePath = savePathRoot + fileName

    print("url " + url_address)
    print("savePath " + savePath)

    response = get(url_address)
    if response.status_code == 200:
        urllib.request.urlretrieve(url_address, savePath, show_progress)
