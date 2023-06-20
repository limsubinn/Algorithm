# pypy3로 제출

import sys
import bisect

def input():
    return sys.stdin.readline().strip()

n = int(input())

A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab, cd = [], [] # A+B, C+D
for i in range(n):
    for j in range(n):
        ab.append(A[i] + B[j])
        cd.append(C[i] + D[j])

ab.sort()
cd.sort()

# ab는 0부터 탐색, cd는 마지막부터 탐색 (합이 0이 되어야 함)
i, j = 0, len(cd)-1
answer = 0

while i < len(ab) and j >= 0:
    temp = ab[i] + cd[j]

    # 합이 0보다 크면 cd 값 감소
    if temp > 0:
        j -= 1
    # 합이 0보다 작으면 ab 값 증가
    elif temp < 0:
        i += 1
    # 합이 0일 때
    else:
        # 각 배열에 같은 값이 몇 개 있는지 확인 후 정답 추가
        abLeft = bisect.bisect_left(ab, ab[i])
        abRight = bisect.bisect_right(ab, ab[i])
        cdLeft = bisect.bisect_left(cd, cd[j])
        cdRight = bisect.bisect_right(cd, cd[j])
        answer += (abRight - abLeft) * (cdRight - cdLeft)

        # 인덱스 조정
        i = abRight
        j = cdLeft - 1

print(answer)

'''
딕셔너리를 이용한 풀이

import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().strip()

n = int(input())

A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = defaultdict(int) # key=합, value=개수
for i in range(n):
    for j in range(n):
        ab[A[i] + B[j]] += 1

answer = 0
for i in range(n):
    for j in range(n):
        k = (C[i] + D[j]) * -1 # ab + cd = 0 이 되어야 함
        if k in ab:
            answer += ab[k]
print(answer)
'''