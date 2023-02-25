# 프로그래머스 87946: 피로도
# 완전 탐색

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons, len(dungeons)):
        cp = k
        res = 0
        
        for j in i:
            if cp >= j[0]:
                cp -= j[1]
                res += 1
        
        answer = max(answer, res)
    
    return answer