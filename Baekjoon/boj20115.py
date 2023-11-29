N = int(input())

drink = list(map(int, input().split()))
drink.sort(reverse = True)
size = len(drink)

while size > 1:
    d = drink.pop()
    size -= 1
    drink[0] += d * 0.5

print("{:.5f}".format(drink[0]))