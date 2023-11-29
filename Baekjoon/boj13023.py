import sys
sys.setrecursionlimit(10**9)

def dfs(i, result):
    global answer
    
    if result >= 5:
        answer = 1
        return

    for j in friends[i]:
        if not visited[j]:
            visited[j] = True
            dfs(j, result+1)
            visited[j] = False

n, m = map(int, input().split())

friends = [[] for _ in range(n)] # 친구 관계 저장
for i in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

global answer
answer = 0

for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i, 1) # 친구 관계 확인
    if answer == 1:
        break
print(answer)