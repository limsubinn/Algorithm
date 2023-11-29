# 프로그래머스 150369: 택배 배달과 수거하기 (2023 KAKAO BLIND RECRUITMENT)

def solution(cap, n, deliveries, pickups):
    answer = 0
    d_temp = 0
    p_temp = 0

    for i in range(n-1, -1, -1):
        cnt = 0
        d_temp += deliveries[i]
        p_temp += pickups[i]

        while d_temp > 0 or p_temp > 0:
            d_temp -= cap
            p_temp -= cap
            cnt += 1

        answer += cnt * (i+1) * 2
                
    return answer