from collections import deque

n, m = map(int, input().split())
miro = [[] for _ in range(n)]

for i in range(n):
    data = input()
    for j in range(m):
        miro[i].append(int(data[j]))


def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        qx, qy = queue.popleft()

        for i in range(4):
            mx = qx + dx[i]
            my = qy + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue

            if miro[mx][my] == 1:
                miro[mx][my] = miro[qx][qy] + 1
                queue.append([mx, my])

    return miro[n-1][m-1]

print(bfs(0,0))