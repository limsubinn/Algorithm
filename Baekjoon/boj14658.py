# 백준 14658: 하늘에서 별똥별이 빗발친다

import sys

def input():
    return sys.stdin.readline().strip()

n, m, l, k = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(k)]
answer = float('INF')

for i in range(k):
    for j in range(k):
        # 꼭짓점 좌표
        x1, x2 = stars[i][0], stars[i][0] + l
        y1, y2 = stars[j][1], stars[j][1] + l

        # 지구에 부딪히는 별똥별의 개수
        result = 0
        for x, y in stars:
            if x < x1 or x > x2 or y < y1 or y > y2:
                result += 1

        # 최솟값 갱신
        answer = min(answer, result)

print(answer)
