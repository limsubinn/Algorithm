# 백준 16928: 뱀과 사다리 게임

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def move_input(num):
    for _ in range(num):
        a, b = map(int, input().split())
        move[a] = b

def bfs(x):
    visited[x] = 0
    queue = deque([x])

    while queue:
        x = queue.popleft()

        # 도착
        if x == 100:
            return visited[x]

        for i in range(1, 7):
            if x+i > 100 or visited[x+i] >= 0:
                continue

            # 사다리 or 뱀
            if move.get(x+i):
                if visited[move[x+i]] >= 0:
                    continue
                mx = move[x+i]
                visited[x+i] = visited[x] + 1
                visited[mx] = visited[x+i]
                queue.append(mx)

            # 주사위
            else:
                queue.append(x+i)
                visited[x+i] = visited[x] + 1

n, m = map(int, input().split())

move = {}
move_input(n)
move_input(m)

visited = [-1] * 101
answer = bfs(1)

print(answer)