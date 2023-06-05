import sys

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] + [10001] * k

for coin in coins:
    for i in range(coin, k+1):
        # i원을 만드는 최소 동전의 개수 = [i-coin]원을 만드는 동전의 개수 + [coin]원
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])