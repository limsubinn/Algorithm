# 프로그래머스 42890: 후보키 (2019 KAKAO BLIND RECRUITMENT)

from itertools import combinations

def solution(relation):
    row_size = len(relation)
    column_size = len(relation[0])
    result = [] # 정답 리스트

    for i in range(1, column_size+1):
        cases = list(combinations(range(column_size), i)) # 후보 키 조합
        for case in cases:
            # 후보 키 리스트
            tmp = [[] for j in range(row_size)]
            for c in case:
                for j in range(row_size):
                    tmp[j].append(relation[j][c])
            for t in range(len(tmp)):
                tp = tuple(tmp[t])
                tmp[t] = tp
            
            if len(set(tmp)) == row_size: # 유일성 체크
                for j in result:
                    if len(set(case) - set(j)) == len(case) - len(j): # 최소성 체크
                        break
                else:
                    result.append(case)

    return len(result)