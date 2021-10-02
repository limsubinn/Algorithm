n = int(input())

cash = [500, 100, 50, 10, 5, 1]
k = 1000 - n
cnt = 0

for i in cash:
    cnt += k // i
    k %= i

print(cnt)