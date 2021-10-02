n=int(input())

for i in range(n):
    ox=str(input())
    cnt=0
    sum=0

    for i in ox:
        if i == "O":
            cnt+=1
        else:
            cnt=0
        sum+=cnt

    print(sum)

