n=int(input())

for i in range(n):
    s=list(map(int,input().split()))
    avg=sum(s[1:])/s[0]
    cnt=0

    for i in s[1:]:
        if i>avg:
            cnt+=1

    print(f"{cnt/s[0]*100:.3f}%")

