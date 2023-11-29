# 프로그래머스 155651: 호텔 대실 

import heapq

def solution(book_time):
    answer = 1
    
    s = []
    for i, j in book_time: # 시간 -> 분 단위로 환산 
        [h1, m1] = i.split(':')
        m1 = int(h1) * 60 + int(m1)
        [h2, m2] = j.split(':')
        m2 = int(h2) * 60 + int(m2)
        s.append([m1, m2])
    s.sort(key = lambda x : x[0]) # 시작 시간 기준으로 정렬 
    
    heap = [] # 최소 힙
    heapq.heappush(heap, s[0][1])
    for i in range(1, len(s)):
        for j in range(i):
            if heap[0] + 10 <= s[i][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, s[i][1])
                break
        else:
            heapq.heappush(heap, s[i][1])
            answer += 1
            
    return answer