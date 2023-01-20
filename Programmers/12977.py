# 프로그래머스 12977: 소수 만들기

from itertools import combinations

def solution(nums):    
    cnt = 0
    ans = 0
    
    for i in list(combinations(nums, 3)):
        cnt += 1
        res = sum(i)
        for j in range(2, res):
            if res % j == 0:
                ans += 1
                break

    return cnt - ans

'''
for-else 구문도 존재
'''