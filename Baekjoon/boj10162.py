import sys
t = int(sys.stdin.readline())
time = [300, 60, 10]
cnt = []

for i in time:
    cnt.append(t // i)
    t %= i

if t == 0:
    print(cnt[0], cnt[1], cnt[2])
else:
    print(-1)