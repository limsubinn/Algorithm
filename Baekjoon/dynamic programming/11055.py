n = int(input())
a = list(map(int, input().split()))

dp = [a[i] for i in range(n)]

for i in range(1, n):
    for j in range(i):
        # 증가하는 부분 수열
        if a[j] < a[i]:
            # 최댓값 갱신
            dp[i] = max(dp[i], dp[j] + a[i])
print(max(dp))