# bfs

from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()

    if list[y][x] == 1:
        queue.append([y, x])
        list[y][x] = 0

        while queue:
            q1, q2 = queue.popleft()

            for i in range(4):
                mx = q2 + dx[i]
                my = q1 + dy[i]

                if mx < 0 or mx >= m or my < 0 or my >= n:
                    continue

                if list[my][mx] == 1:
                    queue.append([my, mx])
                    list[my][mx] = 0
        return True
    else:
        return False

t = int(input())
count = []

for i in range(t):
    m, n, k = map(int, input().split())
    list = [[0] * m for _ in range(n)]
    count.append(0)

    for j in range(k):
        x, y = map(int, input().split())
        list[y][x] = 1

    for a in range(n):
        for b in range(m):
            if bfs(b, a):
                count[i] += 1

for i in range(t):
    print(count[i])