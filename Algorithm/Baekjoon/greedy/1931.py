n = int(input())
time = []

for i in range(n):
    start, end = map(int, input().split())
    time.append((end, start))

time.sort()
cnt = 0
end = 0

for i in range(n):
    if time[i][1] >= end:
        cnt += 1
        end = time[i][0]

print(cnt)