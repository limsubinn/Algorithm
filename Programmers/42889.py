# 프로그래머스 42889: 실패율 (2019 KAKAO BLIND RECRUITMENT)

import numpy

def solution(N, stages):
    arrive = [0 for i in range(N)]
    clear = [0 for i in range(N)]
    for i in stages:
        for j in range(i-1):
            arrive[j] += 1
            clear[j] += 1
        if i <= N:
            arrive[i-1] += 1
    
    res = {}
    for i in range(N):
        if arrive[i] == 0:
            res[i+1] = 0
        else:
            res[i+1] = 1 - clear[i] / arrive[i]
    res = list(dict(sorted(res.items(), key=lambda x:x[1], reverse=1)).keys())
    
    return res