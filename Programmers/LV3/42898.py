# 프로그래머스 42898: 등굣길

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for x in range(1, n+1):
        for y in range(1, m+1):
            if x == 1 and y == 1: # 집이 있는 곳
                continue
            if [y, x] in puddles: # 물이 잠긴 지역
                continue
            dp[x][y] = dp[x-1][y] + dp[x][y-1] 

    return (dp[-1][-1]) % 1000000007