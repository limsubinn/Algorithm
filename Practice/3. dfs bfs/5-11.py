from collections import deque

n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input())))

print(l)

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 이동 방향 정의
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    count = 10

    while queue:
        x, y = queue.popleft()
        print(x, y)
        count -= 1

        for j in range(4):
            mx = x + dx[j]
            my = y + dy[j]

            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue

            if l[mx][my] == 0:
                continue

            if l[mx][my] == 1:
                l[mx][my] == l[x][y] + 1
                queue.append((mx, my))
                print(queue)

    return l[n-1][m-1]

print(bfs(0,0))