# 프로그래머스 92341: 주차 요금 계산 (2022 KAKAO BLIND RECRUITMENT)

import math

def solution(fees, records):
    car = []
    dic = {}
    for i in records: # 딕셔너리에 저장 {차량 번호: 시간}
        j = i.split()
        if j[1] in dic:
            dic[j[1]].append(j[0])
        else:
            car.append(j[1])
            dic[j[1]] = [j[0]]
        
    for i in car:
        time = -1
        total = 0
        for j in dic[i]: # 각 딕셔너리를 순회하면서 누적 주차 시간 계산
            h = int(j.split(':')[0])
            m = int(j.split(':')[1])
            
            if time == -1:
                time = h * 60 + m
            else:
                time = h * 60 + m - time
                total += time
                time = -1
        if time != -1:
            total += (23*60+59) - time
        
        # 주차 요금 계산
        if total > fees[0]:
            dic[i] = fees[1] + math.ceil((total-fees[0]) / fees[2]) * fees[3]
        else:
            dic[i] = fees[1]
        
    dic = sorted(dic.items()) # key값으로 정렬
    
    answer = []
    for i, j in dic:
        answer.append(j)
    
    return answer