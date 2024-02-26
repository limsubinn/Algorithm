# 백준 5052: 전화번호 목록

import sys

def input():
    return sys.stdin.readline().strip()

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = sorted([input() for _ in range(n)]) # 정렬

    for i in range(1, n):
        # 한 번호가 다른 번호의 접두어인 경우
        if numbers[i-1] == numbers[i][:len(numbers[i-1])]:
            print("NO")
            break
    else:
        print("YES")
