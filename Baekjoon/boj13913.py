# 백준 13913: 숨바꼭질 4

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(n, k):
    queue = deque([n])
    visited[n] = 1

    while queue:
        n = queue.popleft()

        # 수빈이가 동생을 찾았을 경우
        if n == k:
            return visited[n]

        # 이동
        for i in [n*2, n+1, n-1]:
            if 0 <= i <= 200000 and not visited[i]:
                queue.append(i)
                visited[i] = visited[n] + 1
                path[i] = n # 경로 표시

n, k = map(int, input().split())
visited = [0] * 200001
path = [0] * 200001

# 가장 빠른 시간
time = bfs(n, k)

# 이동 경로
result = [k]
for i in range(time-1):
    result.append(path[k])
    k = path[k]
result.reverse() # 뒤집기

print(time-1)
print(*result)