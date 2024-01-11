# 백준 17404: RGB거리 2

import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
answer = float('INF')

for k in range(3):
    result = [[float('INF')] * 3 for _ in range(n)] # 초기화
    result[0][k] = costs[0][k] # 첫 번째 집 -> k번째 선택

    # 최소 비용 구하기
    for i in range(1, n):
        result[i][0] = costs[i][0] + min(result[i-1][1], result[i-1][2])
        result[i][1] = costs[i][1] + min(result[i-1][0], result[i-1][2])
        result[i][2] = costs[i][2] + min(result[i-1][0], result[i-1][1])

    # 마지막 집 -> k번째 선택 X
    for i in range(3):
        if i != k:
            answer = min(answer, result[-1][i])

print(answer)