# 백준 11003: 최솟값 찾기

from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))

queue = deque()
queue.append((0, a[0]))

for i in range(1, l):
    print(queue[0][1], end=' ')

    while queue and queue[-1][1] > a[i]:
        queue.pop()

    queue.append((i, a[i]))

for i in range(l, n):
    print(queue[0][1], end=' ')

    if queue[0][0] == i - l:
        queue.popleft()

    while queue and queue[-1][1] > a[i]:
        queue.pop()

    queue.append((i, a[i]))

print(queue[0][1])