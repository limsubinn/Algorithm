n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

minimum = price[0]
cost = 0

for i in range(n-1):
    if minimum > price[i]:
        minimum = price[i]

    cost += minimum * length[i]

print(cost)