# 프로그래머스 42889: 실패율 (2019 KAKAO BLIND RECRUITMENT)

import numpy

def solution(N, stages):
    answer = {}
    
    arrive = [0 for i in range(N)]
    stay = [0 for i in range(N)]

    arrive[0] = len(stages)
    stay[0] = stages.count(1)
    answer[1] = stay[0] / arrive[0]
    

    for i in range(1, N):
        arrive[i] = arrive[i-1] - stay[i-1]
        stay[i] = stages.count(i+1)

        if arrive[i] == 0:
            answer[i+1] = 0
        else:
            answer[i+1] = stay[i] / arrive[i]

    answer = list(dict(sorted(answer.items(), key=lambda x:x[1], reverse=1)).keys())
    
    return answer