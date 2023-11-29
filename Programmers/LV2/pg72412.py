# 프로그래머스 72412: 순위 검색 (2021 KAKAO BLIND RECRUITMENT)

from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = [0] * len(query)
    
    dic = {}
    for i in info:
        i = i.split()
        pick = tuple(i[:4])
        score = int(i[4])

        # 각 info에 대해 탐색될 수 있는 모든 경우의 수를 딕셔너리에 추가 {(query):[score]}
        for j in range(5):
            combi = list(combinations(pick, j))
            for c in combi:
                if c in dic:
                    dic[c].append(score)
                else:
                    dic[c] = [score]
    
    for key in dic: # 이진 탐색을 위한 정렬
        dic[key].sort()

    for i in range(len(query)):
        q = query[i].replace("and", "").replace("-", "").split()
        
        # query
        if len(q) == 1:
            con = ()
        else:
            con = tuple(q[:-1])
        
        # score
        sc = int(q[-1])

        # Lower Bound
        if con in dic:
            pos = bisect_left(dic[con], sc)
            answer[i] = len(dic[con]) - pos
        
    return answer