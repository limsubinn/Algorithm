# 프로그래머스 12979: 기지국 설치

def solution(n, stations, w):
    answer = 0
    k = 1
    t = n+1

    for i in stations:
        if i+w >= n:
            t = i-w
            break
        if i-w < 1:
            k = i+w+1
            continue
        
        res = i-w-k # 기지국의 전파가 닿지 않는 공간
        cnt = 0 # 설치할 기지국의 수
        while 2*w+1 <= res:
            res -= 2*w + 1
            cnt += 1
        if res > 0:
            cnt += 1
        answer += cnt

        k = i+w+1    

    # 끝에 남은 공간 수행
    res = t-k
    cnt = 0
    while 2*w+1 <= res:
        res -= 2*w + 1
        cnt += 1
    if res > 0:
        cnt += 1
    answer += cnt

    return answer