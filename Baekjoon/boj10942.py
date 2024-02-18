# 백준 10942: 팰린드롬?

import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
num = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
for j in range(n):
    for i in range(j+1):
        # 한 글자일 경우 -> 팰린드롬 O
        if i == j:
            dp[i][j] = 1
            continue
        # 맨 앞의 숫자 == 맨 뒤의 숫자 이고,
        # 두 글자 or 그 전까지의 수가 팰린드롬인 경우 -> 팰린드롬 O
        if num[i] == num[j] and (j - i == 1 or dp[i+1][j-1] == 1):
            dp[i][j] = 1
        # 나머지 -> 팰린드롬 X

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
