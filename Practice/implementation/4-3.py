p = input()
x = int(p[1])
y = int(ord(p[0]) - ord('a')) + 1

move = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
count = 8

for i, j in move:
    mx = x - i
    my = y - j

    if mx < 1 or my < 1 or mx > 8 or my > 8:
        count -= 1

print(count)