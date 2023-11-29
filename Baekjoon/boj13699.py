n = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(1, n+1):
    for k in range(n):
        dp[i] += dp[k] * dp[i-1-k]

print(dp[-1])