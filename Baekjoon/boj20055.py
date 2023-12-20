# 백준 20055: 컨베이어 벨트 위의 로봇

import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def rotate(v):
    if v == 0:
        return 2 * n - 1
    else:
        return v - 1

def check_end(k):
    result = 0
    for b in belt:
        if b > 0:
            continue
        result += 1
        if result >= k:
            return True
    return False


n, k = map(int, input().split())
belt = list(map(int, input().split()))

# 올리는 위치
i = 0
# 내리는 위치
o = n-1

# 로봇
queue = deque()
visited = [False] * 2 * n
cnt = 0 # 로봇의 개수

answer = 1
while True:
    # 벨트 회전
    i = rotate(i)
    o = rotate(o)

    temp = cnt

    # 로봇 이동
    for _ in range(cnt):
        position = queue.popleft()

        # 내리기
        if position == o:
            visited[position] = False
            temp -= 1
            continue

        # 다음 위치
        if position == 2 * n - 1:
            next = 0
        else:
            next = position + 1

        # 내리기
        if next == o and belt[next] > 0:
            visited[position] = False
            belt[next] -= 1
            temp -= 1
            continue

        # 로봇이 이동할 수 있는 경우
        if not visited[next] and belt[next] >= 1:
            visited[position] = False
            visited[next] = True
            belt[next] -= 1
            queue.append(next)
        # 로봇이 이동할 수 없는 경우
        else:
            queue.append(position)

    cnt = temp

    # 로봇 올리기
    if belt[i] != 0:
        queue.append(i)
        visited[i] = True
        belt[i] -= 1
        cnt += 1

    # 내구도 == 0 인 칸의 개수 >= k 인 경우
    if check_end(k):
        break

    answer += 1

print(answer)
