# pypy3로 제출

import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 누적합
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + array[i-1][j-1] - dp[i-1][j-1]

# 부분행렬의 최댓값
answer = -10000
for x1 in range(1, n+1):
    for y1 in range(1, m+1):
        for x2 in range(x1, n+1):
            for y2 in range(y1, m+1):
                res = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
                if res > answer:
                    answer = res

print(answer)