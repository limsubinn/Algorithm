# 이진 탐색
# 실전 문제1. 부품 찾기

n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))

n_array.sort()

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if n_array[mid] == target:
            return True
        elif n_array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False

for i in m_array:
    if binary_search(0, n-1, i):
        print('yes', end=' ')
    else:
        print('no', end=' ')