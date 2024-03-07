# 프로그래머스 154538: 숫자 변환하기

from collections import deque

def bfs(x, y, n):
    queue = deque()
    queue.append([x, 0])

    MAX_VALUE = 1_000_001
    visited = [False] * MAX_VALUE
    visited[x] = True

    while queue:
        x, cnt = queue.popleft()

        if x == y:
            return cnt

        # x+n, x*2, x*3
        for i in [n, x, x * 2]:
            if x + i < MAX_VALUE and not visited[x + i]:
                visited[x + i] = True
                queue.append([x + i, cnt + 1])

    return -1

def solution(x, y, n):
    answer = bfs(x, y, n)
    return answer