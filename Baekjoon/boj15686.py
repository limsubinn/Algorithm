import sys
from itertools import combinations

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

chicken = [] # 치킨 집을 저장할 리스트
house = [] # 집을 저장할 리스트

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        # 치킨집
        if temp[j] == 2:
            chicken.append([i ,j])
            continue
        # 집
        if temp[j] == 1:
            house.append([i, j])

answer = float('INF')

# 각 조합에 대해
for combination in list(combinations(chicken, m)):
    result = 0
    # 각 집마다
    for hx, hy in house:
        dist = float('INF')
        # 치킨 집과의 최소 거리 계산
        for cx, cy in combination:
            dist = min(dist, abs(cx - hx) + abs(cy - hy))
        result += dist
    # 최소 치킨 거리 갱신
    answer = min(answer, result)

print(answer)