# 이진 탐색
# 실전 문제1. 부품 찾기
# 교재 코드 - 집합 자료형 이용

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')