from collections import deque
from itertools import combinations
import copy

def bfs(x, y, temp, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([x, y])

    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= len(temp) or my < 0 or my >= len(temp[0]):
                continue

            if visited[mx][my]:
                continue

            if temp[mx][my] == 1:
                continue

            temp[mx][my] = 2
            queue.append([mx, my])
            visited[mx][my] = True

n, m = map(int, input().split())

lab = []
for i in range(n):
    lab.append(list(map(int, input().split())))

walls = [] # 벽을 세울 수 있는 곳의 좌표 저장
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            walls.append([i, j])

answer = 0
combi = list(combinations(walls, 3)) # 벽을 세울 곳

for com in combi:
    temp = copy.deepcopy(lab)
    visited = [[False] * m for _ in range(n)]
    for c in com:
        temp[c[0]][c[1]] = 1 # 벽 세우기
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 2: # 바이러스 확산
                bfs(x, y, temp, visited)
    cnt = 0
    for i in temp:
        cnt += i.count(0) # 안전 영역의 수
    answer = max(answer, cnt)

print(answer)