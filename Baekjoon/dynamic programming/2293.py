import sys

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1 # 동전 하나를 사용하는 경우

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[-1])