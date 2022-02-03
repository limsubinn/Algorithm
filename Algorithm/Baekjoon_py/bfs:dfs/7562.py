from collections import deque

t = int(input())

def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append([x1, y1])

    chess[x1][y1] = 1

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    while queue:
        qx, qy = queue.popleft()

        if qx == x2 and qy == y2:
            print(chess[qx][qy] - 1)
            break

        for i in range(8):
            x = qx + dx[i]
            y = qy + dy[i]

            if x < 0 or x >= n or y < 0 or y >= n:
                continue

            if chess[x][y] == 0:
                queue.append([x, y])
                chess[x][y] = chess[qx][qy] + 1


for i in range(t):
    n = int(input())
    chess = [[0 for _ in range(n)] for _ in range(n)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    bfs(start[0], start[1], end[0], end[1])