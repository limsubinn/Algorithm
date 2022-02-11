import sys

k, n = map(int, sys.stdin.readline().split())
cable = []

for i in range(k):
    cable.append(int(sys.stdin.readline()))

start = 1
end = max(cable)

result = 0
while start <= end:
    cut = 0
    mid = (start + end) // 2

    for i in cable:
        cut += i // mid

    if cut >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
