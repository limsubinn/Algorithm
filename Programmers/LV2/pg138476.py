# 프로그래머스 138476: 귤 고르기

from collections import Counter

def solution(k, tangerine):
    tan = sorted(Counter(tangerine).values())
    answer = len(tan)
    n = len(tangerine) - k
    
    for i in tan:
        if i < n:
            answer -= 1
            n -= i
        elif i == n:
            return answer - 1
        else:
            return answer

'''
collections 모듈의 Counter 클래스 -> 요소들의 개수를 딕셔너리로 만들어준다.
'''