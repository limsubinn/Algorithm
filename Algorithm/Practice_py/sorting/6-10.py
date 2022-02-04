# 정렬
# 실전 문제1. 위에서 아래로

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

num.sort(reverse=1)
for i in num:
    print(i, end=' ')