import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

# 연속된 좌석의 개수에 따른 좌석 이동 가능한 경우의 수
dp = [0] * 41
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

start = 1
answer = 1

# 고정석을 기준으로 좌석을 잘라서 이동 가능한 경우의 수
vip.sort()
for i in vip:
    if start != i:
        answer *= dp[i - start]
    start = i+1

# 마지막에 남은 좌석
if start < n+1:
    answer *= dp[(n+1) - start]

print(answer)