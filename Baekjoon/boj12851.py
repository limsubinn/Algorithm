# 백준 12851: 숨바꼭질 2

from collections import deque

def bfs(n, k, t):
    global time
    cnt = 0

    queue = deque()
    queue.append([n, t])

    visited = [float('INF')] * 100001
    visited[n] = 0

    while queue:
        x, t = queue.popleft()

        # 수빈이가 동생을 찾는 가장 빠른 시간
        if x == k and t <= time:
            cnt += 1  # 방법의 수 증가
            time = t
            continue

        for i in [x - 1, x + 1, 2 * x]:
            # 이동
            if 0 <= i <= 100000 and visited[i] >= visited[x] + 1:
                visited[i] = visited[x] + 1
                queue.append([i, t + 1])

    return cnt

n, k = map(int, input().split())
time = float('INF') # 수빈이가 동생을 찾는 가장 빠른 시간
cnt = bfs(n, k, 0) # 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수

print(time)
print(cnt)
