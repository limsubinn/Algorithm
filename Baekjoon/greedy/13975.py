import sys
import heapq

def input():
    return sys.stdin.readline().strip()

T = int(input())

for i in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    heapq.heapify(files)
    answer = 0

    while True:
        # 제일 작은 값 2개를 빼서 더한 후 다시 넣는다.
        h1 = heapq.heappop(files)
        h2 = heapq.heappop(files)
        answer += h1 + h2
        if not files:
            break
        heapq.heappush(files, h1 + h2)

    print(answer)