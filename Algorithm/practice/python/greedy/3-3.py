n, m = map(int, input().split())
res = 0

for i in range(n):
        cards = list(map(int, input().split()))
        if res < min(cards):
                res = min(cards)

print(res)