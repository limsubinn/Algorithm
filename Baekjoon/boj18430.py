# 백준 18430: 무기 공학

import sys

def input():
    return sys.stdin.readline().strip()

def can_make(x, y, b):
    for i in range(x, x+2):
        for j in range(y, y+2):
            if boomerang[b][i-x][j-y] and visited[i][j]:
                return False
    return True

def make(x, y, b):
    result = 0
    for i in range(x, x+2):
        for j in range(y, y+2):
            value = boomerang[b][i-x][j-y]
            if value:
                result += value * trees[i][j]
                visited[i][j] = True
    return result

def revert(x, y, b):
    for i in range(x, x+2):
        for j in range(y, y+2):
            value = boomerang[b][i - x][j - y]
            if value:
                visited[i][j] = False

def solution(x, y, result):
    global answer

    # 그래프를 모두 탐색한 경우
    if x+1 >= n:
        answer = max(answer, result) # 정답 갱신
        return

    # x행을 모두 탐색한 경우
    if y+1 >= m:
        solution(x+1, 0, result) # 다음 행 탐색
        return

    for i in range(4):
        if not can_make(x, y, i):
            continue
        # 부메랑을 만드는 경우
        solution(x, y+1, result + make(x, y, i)) # 다음 칸 탐색
        revert(x, y, i) # 되돌리기

    # 부메랑을 만들지 않는 경우
    solution(x, y+1, result)  # 다음 칸 탐색

n, m = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

answer = 0
boomerang = [
    [[1, 2], [0, 1]],
    [[0, 1], [1, 2]],
    [[1, 0], [2, 1]],
    [[2, 1], [1, 0]],
]

solution(0, 0, 0)
print(answer)
