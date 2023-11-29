n, m = map(int, input().split())

# 팩토리얼
dp = [1] * (n+1)
for i in range(2, n+1):
    dp[i] = i * dp[i-1]

answer = dp[n] // (dp[m] * dp[n-m])
print(answer)