# 프로그래머스 12927: 야근 지수

import heapq

def solution(n, works):
    # 우선순위 큐 (내림차순)
    heap = []
    for work in works:
        heapq.heappush(heap, -work)

    # n개만큼 꺼내서 작업량 1씩 빼고 다시 넣기
    for i in range(n):
        h = heapq.heappop(heap)
        if h >= 0:
            break
        heapq.heappush(heap, h + 1)

    # 야근 지수 구하기
    answer = 0
    while heap:
        h = heapq.heappop(heap)
        answer += h ** 2

    return answer
