n = int(input())

dp = [[0, 0] for _ in range(n)]
dp[0][0] = 0
dp[0][1] = 1

# 각 자릿수 별 이친수의 개수
for i in range(1, n):
    # 끝이 0인 이친수 -> 전 값에서 모든 이친수의 개수
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    # 끝이 1인 이친수 -> 전 값에서 0으로 끝나는 이친수의 개수
    dp[i][1] = dp[i-1][0]

answer = dp[-1][0] + dp[-1][1]
print(answer)