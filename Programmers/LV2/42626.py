# 프로그래머스 42626: 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            return answer
        if len(scoville) == 1:
            return -1
        
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1 + s2 * 2)
        answer += 1
        
'''
정확성 테스트(O), 효율성 테스트(X)

def solution(scoville, K):
    answer = 0
    
    while True:
        scoville.sort()
        
        if scoville[0] >= K:
            return answer
        if len(scoville) == 1:
            return -1
        
        s = [scoville[0] + scoville[1] * 2]
        scoville = s + scoville[2:]
        answer += 1
'''