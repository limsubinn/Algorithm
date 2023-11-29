import sys

n, c = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()

start = 1
end = house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    count = 1
    current = house[0]

    for i in house:
        if current + mid <= i:
            count += 1
            current = i

    if count < c:
        end = mid - 1
    else:
        start = mid + 1

print(end)