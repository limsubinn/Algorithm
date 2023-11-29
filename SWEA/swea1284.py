# 1284. 수도 요금 경쟁

T = int(input())

for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    a = P * W
    b = Q
    if W > R:
        b += (W - R) * S
    
    answer = min(a, b)
    print(f'#{t} {answer}')