# 백준 2166: 다각형의 면적

import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.append(points[0])

a, b = 1, 1
for i in range(n):
    a += points[i][0] * points[i+1][1]
    b += points[i][1] * points[i+1][0]

answer = round((b - a) / 2, 1) # 소수점 아래 둘째 자리에서 반올림
print(abs(answer))