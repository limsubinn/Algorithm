c, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 인덱스: 확보해야 하는 고객 수
# 값: 최소 비용
# c보다 많은 고객 수에서 최소 비용이 나올 수 있다.
# 주어지는 비용의 최댓값 = 100
dp = [0] + [float('INF')] * (c + 100)

for cost, people in array:
    for i in range(1, c+101):
        dp[i] = min(dp[i-people] + cost, dp[i])

print(min(dp[c:]))