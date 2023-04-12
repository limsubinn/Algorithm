n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    result = 4
    for j in range(1, int(i**0.5)+1):
        result = min(result, dp[i - j**2])
    dp.append(result + 1)

print(dp[n])