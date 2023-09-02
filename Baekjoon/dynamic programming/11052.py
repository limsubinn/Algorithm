import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
cards = list(map(int, input().split()))
dp = [0] + [cards[i] for i in range(n)]

# 구매할 카드의 개수별 최댓값을 저장
for i in range(1, n+1):
    for j in range(i//2+1):
        dp[i] = max(dp[i-j] + dp[j], dp[i])

print(dp[n])