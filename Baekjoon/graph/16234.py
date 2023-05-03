from collections import deque

def find(x, y, n, l, r):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[x][y] = True

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or mx >= n or my < 0 or my >= n:
            continue

        if visited[mx][my]:
            continue

        if l <= abs(land[x][y] - land[mx][my]) <= r:
            temp[x][y].append([mx, my])
            temp[mx][my].append([x, y])

def connect(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    people = 0
    space = 0

    while queue:
        x, y = queue.popleft()
        spaces.append([x, y])
        people += land[x][y]
        space += 1

        for tx, ty in temp[x][y]:
            if visited[tx][ty]:
                continue
            queue.append([tx, ty])
            visited[tx][ty] = True
    

    return people // space

n, l, r = map(int, input().split())

land = []
for i in range(n):
    land.append(list(map(int, input().split())))

answer = 0

while True:
    visited = [[False] * n for _ in range(n)]
    temp = [[[] for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            find(i, j, n, l, r) # 연결할 수 있는 좌표 찾기

    check = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j]:
                check = 1
    if check == 0: # 연결할 수 있는 좌표가 없으면 반복문 종료
        break

    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            spaces = []
            if temp[i][j] and not visited[i][j]:
                # 인구 이동
                res = connect(i, j)
                for sx, sy in spaces:
                    land[sx][sy] = res

    answer += 1

print(answer)