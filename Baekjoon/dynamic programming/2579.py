n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

d = [0] * (n+1)
d[1] = arr[1]

if n >= 2:
    d[2] = arr[1] + arr[2]

for i in range(3, n+1):
    d[i] = max(d[i-3] + arr[i-1], d[i-2]) + arr[i]

print(d[n])