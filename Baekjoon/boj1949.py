# 백준 1949: 우수 마을

import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().strip()

def dfs(x):
    visited[x] = True
    for g in graph[x]:
        if not visited[g]:
            dfs(g)
            dp[x][0] += max(dp[g][0], dp[g][1]) # 현재 마을을 우수 마을로 선정하지 않는 경우
            dp[x][1] += dp[g][0] # 현재 마을을 우수 마을로 선정하는 경우

n = int(input())
costs = [0] + list(map(int, input().split()))

dp = [[0, costs[i]] for i in range(n+1)]
visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
answer = max(dp[1][0], dp[1][1])
print(answer)
