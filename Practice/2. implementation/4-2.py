n = int(input())
a = (n+1) * 6 * 10 * 6 * 10

if n >= 3:
    b = n * 5 * 9 * 5 * 9
else:
    b = (n+1) * 5 * 9 * 5 * 9

print(a-b)