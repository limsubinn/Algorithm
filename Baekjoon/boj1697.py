from collections import deque

MAX = 100000
n, k = map(int, input().split())
queue = deque()
queue.append(n)
visited = [0] * (MAX + 1)

while queue:
    q = queue.popleft()
    mv = [q + 1, q - 1, 2 * q]

    if q == k:
        print(visited[q])
        break

    for i in mv:
        if 0 <= i <= MAX and visited[i] == 0:
            visited[i] = visited[q] + 1
            queue.append(i)