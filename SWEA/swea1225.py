# 1225. 암호 생성기

for _ in range(1, 11):
    t = int(input())
    data = list(map(int, input().split()))

    while data[-1] != 0:
        # 사이클
        for i in range(5):
            d = data[i] - (i+1)
            if d > 0:
                data.append(d)
            else:
                data.append(0)
                break
        data = data[i+1:]
    
    print(f'#{t} ', end='')
    for d in data:
        print(d, end=' ')
    print()