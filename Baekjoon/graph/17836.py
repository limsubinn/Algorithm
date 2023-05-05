from collections import deque

def bfs(visited, start, target, flag):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([start[0], start[1]])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or mx >= len(castle) or my < 0 or my >= len(castle[0]):
                continue

            if not flag and castle[mx][my] == 1:
                continue

            if mx == 0 and my == 0:
                continue

            if visited[mx][my] != 0:
                continue

            visited[mx][my] = visited[x][y] + 1
            if mx == target[0] and my == target[1]:
                break
            queue.append([mx, my])
    return visited

def check_result(t):
    result = 0
    if visited[-1][-1] <= t:
        result = visited[-1][-1]
    return result

def bfs_all(m, n, start, target):
    visited = [[0] * m for _ in range(n)]
    bfs(visited, start, target, False)
    return visited

def bfs_part(visited, m, n, start, target):
    v = visited[start[0]][start[1]]
    visited = [[0] * m for _ in range(n)]
    visited[start[0]][start[1]] = v
    bfs(visited, start, target, True)
    return visited
    
n, m, t = map(int, input().split())

castle = []
for i in range(n):
    c = list(map(int, input().split()))
    castle.append(c)

    if 2 in c:
        idx = [i, c.index(2)] # 그람이 있는 곳의 좌표

visited = bfs_all(m, n, [0, 0], [n-1, m-1]) # 전체 탐색
result1 = check_result(t)

# 전체 탐색 시 그람을 찾았을 경우
if visited[idx[0]][idx[1]] != 0:
    # 그람 위치~도착지 탐색
    visited = bfs_part(visited, m, n, idx, [n-1, m-1])
# 전체 탐색 시 그람을 찾지 못했을 경우
else:
    # 그람이 있는 곳까지 탐색
    visited = bfs_all(m, n, [0, 0], idx)
    # 그람을 찾았을 경우
    if visited[idx[0]][idx[1]] != 0:
        # 그람 위치~도착지 탐색
        visited = bfs_part(visited, m, n, idx, [n-1, m-1])
result2 = check_result(t)

if result1 == 0 and result2 == 0:
    print("Fail")
elif result1 == 0:
    print(result2)
elif result2 == 0:
    print(result1)
else:
    print(min(result1, result2))

