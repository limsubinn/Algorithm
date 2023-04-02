# 프로그래머스 42627: 디스크 컨트롤러

import heapq

def solution(jobs):
    jobs.sort(key=lambda x:x[0]) # 요청 시간 순으로 정렬
    heap = []
    answer = 0
    cnt = 0 # 작업 개수
    start, end = -1, 0 # 이전에 작업을 시작한 시간, 종료한 시간
    
    while cnt < len(jobs):
        for j in jobs:
            # 현재 시점에서 작업을 처리할 수 있을 때, 힙에 넣는다.
            if start < j[0] <= end:
                heapq.heappush(heap, j[::-1]) # 작업 시간 순으로
        
        # 처리할 수 없는 작업이 존재하지 않을 경우, 처리 시간을 늘려준다.
        if not heap:
            end += 1
            continue
        
        # 정답 추가
        h = heapq.heappop(heap)
        start = end
        end += h[0]
        answer += end - h[1]
        cnt += 1
        
    return answer // len(jobs)