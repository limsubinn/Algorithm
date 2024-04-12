# 프로그래머스 142085: 디펜스 게임

import heapq

def solution(n, k, enemy):
    s = 0
    queue = []
    heapq.heappush(queue, enemy[0])

    for i in range(len(enemy)):
        # 병사 더하기
        heapq.heappush(queue, -enemy[i])  # 내림차순
        s += enemy[i]

        # 적의 수 > 남은 병사의 수
        if s > n:
            # `무적권`을 사용할 수 없는 경우
            if k == 0:
                return i
            # `무적권`을 사용하는 경우
            s += heapq.heappop(queue)
            k -= 1

    return i + 1