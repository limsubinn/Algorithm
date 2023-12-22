# 백준 14500: 테트로미노

import sys

def input():
    return sys.stdin.readline().strip()

def dfs(x, y, result, cnt):
    global answer

    # 현재 값에 제일 큰 값을 다 더해도 최댓값보다 작은 경우
    if answer >= result + max_value * (4 - cnt):
        return

    # 테트로미노가 완성된 경우
    if cnt == 4:
        answer = max(answer, result)
        return

    # 이동
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or mx >= n or my < 0 or my >= m or visited[mx][my]:
            continue

        # ㅓ, ㅏ, ㅗ, ㅜ 모양
        if cnt == 2:
            visited[mx][my] = True
            dfs(x, y, result + paper[mx][my], cnt + 1)
            visited[mx][my] = False

        visited[mx][my] = True
        dfs(mx, my, result + paper[mx][my], cnt + 1)
        visited[mx][my] = False

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
max_value = max(map(max, paper))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, paper[i][j], 1)
        visited[i][j] = False

print(answer)