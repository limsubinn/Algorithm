from collections import deque

def bfs(x, y):
    cnt = 0

    odd = [[0, 1], [0, -1], [-1, 0], [-1, 1], [1, 0], [1, 1]] # 홀수 이동 좌표
    even = [[0, 1], [0, -1], [-1, -1], [-1, 0], [1, -1], [1, 0]] # 짝수 이동 좌표

    queue = deque()
    queue.append([x, y])

    visited = [[False] * (w+2) for _ in range(h+2)]
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        if x % 2 == 0: # x가 짝수일 때
            for dx, dy in even:
                mx = x + dx
                my = y + dy

                if mx < 0 or mx >= len(array) or my < 0 or my >= len(array[0]):
                    continue

                if array[mx][my] == 1: # 건물이 있는 곳
                    cnt += 1
                    continue
                
                if visited[mx][my]:
                    continue

                queue.append([mx, my])
                visited[mx][my] = True
        else: # x가 홀수일 때
            for dx, dy in odd:
                mx = x + dx
                my = y + dy

                if mx < 0 or mx >= len(array) or my < 0 or my >= len(array[0]):
                    continue

                if array[mx][my] == 1: # 건물이 있는 곳
                    cnt += 1
                    continue
                
                if visited[mx][my]:
                    continue

                queue.append([mx, my])
                visited[mx][my] = True

    return cnt
         
w, h = map(int, input().split())

array = [[0] * (w+2)]
for i in range(h):
    temp = list(map(int, input().split()))
    temp.insert(0, 0)
    temp.append(0)
    array.append(temp)
array.append([0] * (w+2))

answer = bfs(0, 0)
print(answer)