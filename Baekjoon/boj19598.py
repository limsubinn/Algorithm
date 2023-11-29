import sys
import heapq

def input():
    return sys.stdin.readline().strip()

N = int(input())
heap = []
room = [0]

for i in range(N):
    start, end = map(int, input().split())
    heapq.heappush(heap, [start, end])

while heap:
    start, end = heapq.heappop(heap)
    r = heapq.heappop(room)

    if r > start:
        heapq.heappush(room, r)

    heapq.heappush(room, end)

print(len(room))