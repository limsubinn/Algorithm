# 프로그래머스 42747: H-Index

import bisect

def solution(citations):
    citations.sort()
    
    for i in range(len(citations), -1, -1):
        k = bisect.bisect_left(citations, i) # 나머지 논문
        h = len(citations) - k # h번 이상 인용된 논문
        
        if h >= i and k <= i:
            return i
