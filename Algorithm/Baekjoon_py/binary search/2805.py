import sys

n, m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(h)

while start <= end:
    cut = 0
    mid = (start + end) // 2

    for i in h:
        if mid < i:
            cut += i - mid

    if cut >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)