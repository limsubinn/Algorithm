# 백준 2467: 용액

import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
values = list(map(int, input().split()))

start, end = 0, n-1
result = float('INF')

while start < end:
    temp = values[start] + values[end]

    # 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액 찾기
    if abs(result) > abs(temp):
        result = temp
        answer = [values[start], values[end]]

    # 포인터 옮기기
    if temp <= 0:
        start += 1
    else:
        end -= 1

print(*answer)
