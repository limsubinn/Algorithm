# 백준 1461: 도서관

import sys

def input():
    return sys.stdin.readline().strip()

def add(a, b, c):
    global answer
    for i in range(a, b, c):
        answer += abs(books[i]) * 2

n, m = map(int, input().split())
books = list(map(int, input().split()))

books.sort() # 정렬

# (+) 값과 (-) 값의 기준점
for i in range(1, n):
    if books[i-1] < 0 and books[i] > 0:
        mark = i
        break
else:
    if books[-1] < 0:
        mark = n
    else:
        mark = 0

# 가장 절댓값이 큰 값의 인덱스
if abs(books[0]) > abs(books[n-1]):
    max_idx = 0
else:
    max_idx = n-1

# m개씩 묶어서 더하기
answer = -abs(books[max_idx]) # 초기값
add(0, mark, m) # (-)값 더하기
add(n-1, mark-1, -m) # (+)값 더하기

print(answer)
