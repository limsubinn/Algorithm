# 프로그래머스 72412: 순위 검색 (2021 KAKAO BLIND RECRUITMENT) - 수정중,,

from itertools import combinations

def solution(info, query):
    answer = [0] * len(query)
    
    dic = {}
    for i in info:
        i = i.split()
        pick = tuple(i[:4])
        score = int(i[4])

        for j in range(5):
            combi = list(combinations(pick, j))
            for c in combi:
                if c in dic:
                    dic[c].append(score)
                else:
                    dic[c] = [score]
    
    for key in dic:
        dic[key].sort(reverse = True)

    for i in range(len(query)):
        q = query[i].replace("and", "").replace("-", "").split()
        
        if len(q) == 1:
            con = ()
        else:
            con = tuple(q[:-1])
        
        sc = int(q[-1])

        if con in dic:
            for s in dic[con]:
                if s < sc:
                    break
                answer[i] += 1
        
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))