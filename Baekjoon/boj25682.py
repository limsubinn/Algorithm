# 백준 25682: 체스판 다시 칠하기 2

import sys

def input():
    return sys.stdin.readline().strip()

n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]

result = [[0] * (m+1) for _ in range(n+1)]
answer = float('INF')
color = board[0][0]

for i in range(1, n+1):
    for j in range(1, m+1):
        # 맨 왼쪽 위 칸과 색이 같아야 하는 경우
        if (i + j) % 2 == 0:
            r = board[i-1][j-1] != color
        # 맨 왼쪽 위 칸과 색이 달라야 하는 경우
        else:
            r = board[i-1][j-1] == color
        # 누적 합
        result[i][j] = result[i][j-1] + result[i-1][j] - result[i-1][j-1] + r

for i in range(1, n-k+2):
    for j in range(1, m-k+2):
        cnt = result[i+k-1][j+k-1] - result[i+k-1][j-1] - result[i-1][j+k-1] + result[i-1][j-1]
        answer = min(cnt, k*k - cnt, answer)

print(answer)
