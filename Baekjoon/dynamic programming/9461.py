d = [0] * 101
d[1], d[2], d[3] = 1, 1, 1

for i in range(4, 101):
    d[i] = d[i-2] + d[i-3]

t = int(input())
for i in range(t):
    n = int(input())
    print(d[n])