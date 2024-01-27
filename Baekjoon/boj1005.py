# 백준 1005: ACM Craft

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def find():
    result = [0 for _ in range(n+1)] # 각 건물을 건설 완료 하는데 드는 최소 시간
    queue = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            result[i] = time[i]

    while queue:
        cur = queue.popleft()

        for next in graph[cur]:
            indegree[next] -= 1
            result[next] = max(result[next], result[cur] + time[next]) # 시간 갱신

            if indegree[next] == 0:
                queue.append(next)

    return result[w]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split()) # 건물의 개수, 규칙의 개수

    indegree = [0] * (n+1) # 진입 차수
    graph = [[] for _ in range(n+1)] # 그래프
    time = [0] + list(map(int, input().split())) # 각 건물당 건설에 걸리는 시간

    for _ in range(k):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        indegree[b] += 1

    w = int(input()) # 마지막 건물의 번호

    print(find())