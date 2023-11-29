# 프로그래머스 42628: 이중우선순위큐

import heapq

def solution(operations):
    queue = []
    for i in operations:
        i = i.split()
        if i[0] == 'I': # 큐에 주어진 숫자 삽입
            heapq.heappush(queue, int(i[1]))
            continue
        if queue:
            if i[1] == '-1': # 큐에서 최솟값 삭제
                heapq.heappop(queue)
            else: # 큐에서 최댓값 삭제
                queue.sort()
                queue.pop()
    
    if not queue:
        return [0, 0]
    
    queue.sort()
    return [queue[-1], queue[0]]