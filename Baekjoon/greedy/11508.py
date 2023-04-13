import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())

costs = []
for i in range(N):
    costs.append(int(input()))
costs.sort(reverse=True)

res = 0
for i in range(2, len(costs), 3):
    res += costs[i]

answer = sum(costs) - res
print(answer)