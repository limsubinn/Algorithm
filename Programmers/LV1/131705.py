# 프로그래머스 131705: 삼총사

from itertools import combinations

def solution(number):
    answer = 0
    
    for i, j, k in list(combinations(number, 3)):
        if i + j + k == 0:
            answer += 1
            
    return answer