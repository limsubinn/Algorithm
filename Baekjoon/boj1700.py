# 백준 1700: 멀티탭 스케줄링

import sys

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())
electronics = list(map(int, input().split()))

cnt = 0  # 멀티탭에 꽂혀있는 플러그의 개수
holes = [0] * n

answer = 0

for i in range(k):
    e = electronics[i]

    # 이미 플러그가 꽂혀있는 경우
    if e in holes:
        continue

    # 멀티탭에 빈 공간이 있는 경우
    if cnt < n:
        holes[cnt] = e
        cnt += 1
        continue

    # 멀티탭에 빈 공간이 없는 경우
    for j in range(n):
        # 멀티탭에 꽂혀 있는 플러그 중 다시 사용하지 않는 것이 있는 경우
        if holes[j] not in electronics[i+1:k]:
            holes[j] = e
            answer += 1
            break
    # 멀티탭에 꽂혀 있는 플러그 중 다시 사용하지 않는 것이 없는 경우
    else:
        rank = []
        # 가장 나중에 사용하는 플러그 빼기
        for j in range(i+1, k):
            if electronics[j] in holes and electronics[j] not in rank:
                rank.append(electronics[j])
        holes[holes.index(rank[-1])] = e
        answer += 1

print(answer)