# 프로그래머스 68644: 두 개 뽑아서 더하기

from itertools import combinations

def solution(numbers):
    answer = []
    result = list(combinations(numbers, 2))
    
    for i, j in result:
        if i + j not in answer:
            answer.append(i + j)
    
    answer.sort()
    
    return answer