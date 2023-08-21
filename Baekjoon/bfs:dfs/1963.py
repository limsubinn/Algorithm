import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def bfs():
    queue = deque()
    queue.append([a, 0]) # 시작 숫자, 변환 횟수

    visited = [False] * 10000
    visited[a] = True

    while queue:
        q, cnt = queue.popleft()

        # 소수를 변환했을 경우 변환 횟수 리턴
        if q == b:
            return cnt

        q = str(q)

        # 한 자리씩 끊어서 숫자 변환하기
        for i in range(4):
            for j in range(10):
                temp = int(q[:i] + str(j) + q[i+1:])

                # 네 자리수가 아니면 넘어간다.
                if temp < 1000:
                    continue

                # 이미 변환한 적이 있는 수면 넘어간다.
                if visited[temp]:
                    continue

                # 소수가 아니면 넘어간다.
                if not prime[temp]:
                    continue

                queue.append([temp, cnt+1])
                visited[temp] = True

    # 변환이 불가능할 경우
    return "Impossible"

# 소수 리스트
prime = [True] * 10000
prime[0] = prime[1] = False
for i in range(2, 100):
    if prime[i]:
        for j in range(2*i, 10000, i):
            prime[j] = False

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(bfs())

