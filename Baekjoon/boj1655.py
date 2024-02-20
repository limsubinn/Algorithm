# 백준 1655: 가운데를 말해요

import sys
import heapq

def input():
    return sys.stdin.readline().strip()

n = int(input())
left, right = [], []

for i in range(n):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        a = heapq.heappop(left)[1]
        b = heapq.heappop(right)[1]
        heapq.heappush(left, (-b, b))
        heapq.heappush(right, (a, a))

    print(left[0][1])
