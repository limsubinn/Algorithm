n, m = map(int, input().split())
cards = list(map(int, input().split()))
list = []

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] <= m:
                list.append(cards[i] + cards[j] + cards[k])

print(max(list))