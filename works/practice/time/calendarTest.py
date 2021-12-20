import datetime
import calendar

date = datetime.date(2019, 4, 1)

dayTime = date.strftime("%Y%m%d")

print(dayTime)
print(calendar.monthrange(2019, 4))

year, month = 2020, 1
print(calendar.monthrange(year, month)[1])

print("=============================================")


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
            for cur_day in range(1, max_day + 1):
                date = datetime.date(cur_year, cur_month, cur_day)
                if cur_year == e_year and cur_month == e_month and cur_day == e_day + 1:
                    break

                day_time = date.strftime("%Y%m%d")
                result_arr.append(day_time)

    return result_arr


startYear = 2019
startMonth = 4
startDay = 1
endYear = 2020
endMonth = 5
endDay = 5

resultArr = get_time_arr(startYear, startMonth, startDay, endYear, endMonth, endDay)

for idx in range(len(resultArr)):
    print(resultArr[idx])
