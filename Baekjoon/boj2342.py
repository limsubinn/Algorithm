# 백준 2342: Dance Dance Revolution

import sys
sys.setrecursionlimit(10**6)

def move(before, next):
    # 같은 지점으로 이동
    if before == next:
        return 1
    # 중앙에서 이동
    if before == 0:
        return 2
    # 반대편으로 이동
    if abs(next - before) == 2:
        return 4
    # 인접한 지점으로 이동
    return 3

def dfs(order, left, right):
    next = steps[order]

    # 마지막
    if next == 0:
        return 0

    # 이미 방문한 경우
    if dp[order][left][right] != -1:
        return dp[order][left][right]

    dp[order][left][right] = min(dfs(order+1, next, right) + move(left, next), # 왼쪽 움직임
                                 dfs(order+1, left, next) + move(right, next)) # 오른쪽 움직임
    return dp[order][left][right]

steps = list(map(int, input().split()))
n = len(steps)

dp = [[[-1] * 5 for _ in range(5)] for _ in range(n)]
dfs(0, 0, 0)

answer = dp[0][0][0]
print(answer)
