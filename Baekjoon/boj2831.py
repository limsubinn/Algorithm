# 백준 2831: 댄스 파티

import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
men = list(map(int, input().split()))
women = list(map(int, input().split()))

# 정렬
men.sort()
women.sort()

# 투 포인터
answer = 0
start, end = 0, n-1

while start < n and end >= 0:
    man = men[start]
    woman = women[end]

    if man < 0 and woman < 0:
        start += 1
        continue

    if man + woman >= 0:
        end -= 1
        continue

    answer += 1
    start += 1
    end -= 1

print(answer)