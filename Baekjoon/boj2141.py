import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())

town = []
cnt = 0
for i in range(n):
    town.append(list(map(int, input().split())))
    cnt += town[i][1]
town.sort()

res = 0
for ix, ia in town:
    res += ia
    if res >= cnt / 2: # 누적 인구수가 절반을 넘어가는 지점을 구한다.
        print(ix)
        break

'''
시간 초과
거리 * 사람 의 최솟값

import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())

town = []
for i in range(n):
    town.append(list(map(int, input().split())))

result = float('INF')
for ix, ia in town:
    res = 0
    for jx, ja in town:
        res += abs(ix - jx) * ja
    if res < result:
        result = res
        answer = ix

print(answer)
'''