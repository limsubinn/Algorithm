import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
cows = [[] for _ in range(n+1)]

for i in range(n):
    num, pos = map(int, input().split())
    if not cows[num] or cows[num][-1] != pos:
        cows[num].append(pos)

answer = 0
for cow in cows:
    if cow:
        answer += len(cow) - 1
        
print(answer)