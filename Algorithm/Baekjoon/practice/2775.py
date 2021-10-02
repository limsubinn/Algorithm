t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    result = [i+1 for i in range(n)]

    for i in range(k-1):
        for j in range(1,n):
            result[j] += result[j-1]

    print(sum(result))