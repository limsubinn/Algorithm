# 프로그래머스 42586: 기능개발

import heapq
import math

def solution(progresses, speeds):
    answer = []
    heap = []
    
    for i in range(len(progresses)):
        value = math.ceil((100 - progresses[i]) / speeds[i])
        if heap and -value < heap[0]:
            answer.append(len(heap))
            heap = []
        heapq.heappush(heap, -value) # 최대 힙
    
    answer.append(len(heap))
    
    return answer