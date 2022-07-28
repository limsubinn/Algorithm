n=int(input())
k=n
cnt=0

while True:
    m = k//10 + k%10
    k = (k%10)*10 + m%10
    cnt += 1

    if n==k:
        print(cnt)
        break