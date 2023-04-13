import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())

tip = []
for i in range(N):
    tip.append(int(input()))
tip.sort(reverse=True)

answer = 0
for i in range(N):
    res = tip[i] - i
    if res > 0:
        answer += res

print(answer)