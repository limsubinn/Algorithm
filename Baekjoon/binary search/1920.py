import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if a[mid] == target:
            return 1
        elif a[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for i in b:
    print(binary_search(0, n-1, i))