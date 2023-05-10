from collections import deque

n, k = map(int, input().split())
array = list(map(int, input().split()))

queue = deque()
visited = set()
for i in array:
    queue.append([i, 0])
    visited.add(i)

answer = 0
result = 0
while queue:
    x, result = queue.popleft()
    result += 1

    for i in [1, -1]: # 샘터와 인접한 곳 방문
        mx = x + i

        if mx in visited:
            continue

        queue.append([mx, result])
        visited.add(mx)
        answer += result
        k -= 1

        if k <= 0: # 집을 모두 지은 경우
            queue = []
            break

print(answer)