def d(n):
    result=int(n)

    for i in list(str(n)):
        result+=int(i)

    return result

num=[]

for i in range(10000):
    result=d(i+1)
    num.append(result)

for i in range(10000):
    if i+1 not in num:
        print(i+1)
