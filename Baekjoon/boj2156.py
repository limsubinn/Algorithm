n = int(input())
a = [0]
for _ in range(n):
    a.append(int(input()))

d = [0] * (n+1)
d[1] = a[1]

if n >= 2:
    d[2] = a[1] + a[2]

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2] + a[i], d[i-3] + a[i-1] + a[i])

print(d[n])