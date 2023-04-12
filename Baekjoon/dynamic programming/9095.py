T = int(input())

for i in range(T):
    n = int(input())

    dp = [1, 2, 4]
    for j in range(3, n):
        dp.append(dp[j-1] + dp[j-2] + dp[j-3])

    print(dp[n-1])