# 백준 2879: 코딩은 예쁘게

import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
codes = [list(map(int, input().split())) for _ in range(2)]

diff = [codes[1][i] - codes[0][i] for i in range(n)] # 차이값
answer = abs(diff[0])

for i in range(1, n):
    # 부호가 바뀔 때
    if diff[i-1] * diff[i] <= 0:
        answer += abs(diff[i])
    # 큰 차이값 더하기
    else:
        answer += max(abs(diff[i]) - abs(diff[i-1]), 0)

print(answer)
