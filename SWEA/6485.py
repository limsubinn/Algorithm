# 6485. 삼성시의 버스 노선

T = int(input())

for t in range(1, T+1):
    n = int(input())

    station = [0] * 5001
    for _ in range(n):
        a, b = map(int, input().split())
        # 각 버스정류장에 대해 다닐 수 있는 버스 노선 저장
        for i in range(a, b+1):
            station[i] += 1
    
    p = int(input())
    C = [int(input()) for _ in range(p)]
    
    print(f'#{t}', end=' ')
    for c in C:
        print(station[c], end=' ')
    print()