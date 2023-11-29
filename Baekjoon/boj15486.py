import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())

T, P = [0], [0]
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (n+1)
for i in range(1, n+1):
    # 이전까지의 최댓값
    dp[i] = max(dp[i-1], dp[i])
    # i일에 상담을 하는 경우, 상담이 끝나는 날
    end_date = i + T[i] - 1
    # 상담이 끝나는 날이 퇴사일 이전이라면 (상담이 가능한 경우)
    if end_date <= n:
        # 최댓값 갱신 (i일에 상담을 하는 경우, 상담을 하지 않는 경우)
        dp[end_date] = max(dp[i-1] + P[i], dp[end_date])

print(max(dp))