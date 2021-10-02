t = int(input())

for i in range(t):
    r, s = map(str,input().split())

    for i in s:
        print(i*int(r),end='')

    print()