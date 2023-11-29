# BFS를 이용한 풀이
# 플로이드 워셜 알고리즘으로 풀 수 있다.

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def search(x):
    queue = deque()
    queue.append(x)

    while queue:
        q = queue.popleft()

        for i in range(n):
            # 연결되어 있고, 방문한 적이 없으면
            if array[q][i] == 1 and result[x][i] == 0:
                queue.append(i)
                result[x][i] = 1


n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * n for _ in range(n)]
for i in range(n):
    search(i)

for i in result:
    for j in i:
        print(j, end=' ')
    print()
