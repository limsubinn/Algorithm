n, k = map(int, input().split())
a = []
cnt = 0

for i in range(n):
    a.insert(0, int(input()))

for i in a:
    cnt += k // i
    k %= i
    if k == 0:
        break

print(cnt)