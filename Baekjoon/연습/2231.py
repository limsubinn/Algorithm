n = int(input())

for i in range(1, n+1):
    res = i

    for j in range(0, len(str(i))):
        res += int(str(i)[j])

    if res == n:
         print(i)
         break

    if i == n:
        print(0)