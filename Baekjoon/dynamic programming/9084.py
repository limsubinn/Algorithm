import sys

def input():
    return sys.stdin.readline().strip()

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [1] + [0] * m
    for coin in coins:
        for i in range(coin, m+1):
            dp[i] += dp[i-coin]
    print(dp[-1])