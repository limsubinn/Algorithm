import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs(x, y, n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue

            if answer[mx][my] != -1:
                continue

            answer[mx][my] = answer[x][y] + 1
            queue.append([mx, my])

n, m = map(int, input().split())
answer = [[-1 for i in range(m)] for j in range(n)]

for i in range(n): # 그래프 입력 받기
    graph = list(map(int, input().split()))
    for j in range(m):
        if graph[j] == 1:
            continue
        if graph[j] == 0: # 원래 갈 수 없는 땅인 위치
            answer[i][j] = 0
            continue
        if graph[j] == 2: # 목표 지점
            answer[i][j] = 0
            x, y = i, j

bfs(x, y, n, m)
for i in answer:
    for j in i:
        print(j, end=' ')
    print()