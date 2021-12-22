# -*- coding: utf-8 -*-

movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

movie_rank.append('배트맨')
print(movie_rank)

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키')
del movie_rank[3]
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
print(movie_rank)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

nums = [1, 2, 3, 4, 5, 6, 7]
#nums.sort()
#print('max: %d' % nums[-1])
#print('min: %d' % nums[0])
print(max(nums))
print(min(nums))

nums = [1, 2, 3, 4, 5]
print(sum(nums))

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)
