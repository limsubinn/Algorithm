m = int(input())
stocks = list(map(int, input().split()))

money = [m, m]
saved = [0, 0]

for i in range(len(stocks)):
    value = money[0] // stocks[i]
    money[0] -= stocks[i] * value
    saved[0] += value

    if i < 3:
        continue

    if stocks[i-3] > stocks[i-2] > stocks[i-1] > stocks[i]:
        value = money[1] // stocks[i]
        money[1] -= stocks[i] * value
        saved[1] += value
    
    if saved[1] > 0 and stocks[i-3] < stocks[i-2] < stocks[i-1] < stocks[i]:
        money[1] += saved[1] * stocks[i]
        saved[1] = 0

result = [0, 0]
for i in range(2):
    result[i] = money[i] + stocks[-1] * saved[i]

if result[0] > result[1]:
    print("BNP")
elif result[0] < result[1]:
    print("TIMING")
else:
    print("SAMESAME")