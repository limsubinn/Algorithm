# bfs

from collections import deque

n = int(input())
list = [[] for _ in range(n)]

for i in range(n):
    data = input()
    for j in range(n):
        list[i].append(int(data[j]))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    global count
    queue = deque()

    if list[x][y] == 1:
        queue.append([x, y])
        list[x][y] = 0

        while queue:
            q1, q2 = queue.popleft()
            count += 1

            for i in range(4):
                mx = q1 + dx[i]
                my = q2 + dy[i]

                if mx < 0 or mx >= n or my < 0 or my >= n:
                    continue

                if list[mx][my] == 1:
                    queue.append([mx, my])
                    list[mx][my] = 0

    return count

result = 0
cList = []
for i in range(n):
    for j in range(n):
        count = 0
        if bfs(i, j) > 0:
            result += 1
            cList.append(count)

cList.sort()
print(result)
for i in range(len(cList)):
    print(cList[i])