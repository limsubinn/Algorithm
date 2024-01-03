# 백준 9082: 지뢰찾기

import sys

def input():
    return sys.stdin.readline().strip()

t = int(input())

for _ in range(t):
    n = int(input())
    info = list(map(int, input()))
    input()

    answer = 0
    for i in range(n):
        if i == 0:
            if info[i] and info[i+1]:
                info[i] -= 1
                info[i+1] -= 1
                answer += 1
        elif i == n-1:
            if info[i-1] and info[i]:
                info[i-1] -= 1
                info[i] -= 1
                answer += 1
        else:
            if info[i-1] and info[i] and info[i+1]:
                info[i-1] -= 1
                info[i] -= 1
                info[i+1] -= 1
                answer += 1
    print(answer)