# 프로그래머스 67258: 보석 쇼핑

from collections import defaultdict

def solution(gems):
    size = len(gems) # 진열대 전체 길이
    cnt = len(set(gems)) # 보석 종류의 수
    res = size + 1 # 모든 보석을 하나 이상 포함하는 가장 짧은 구간의 길이

    dic = defaultdict(int)
    i = 0

    for j in range(size):
        # 오른쪽 포인터의 보석 증가
        dic[gems[j]] += 1

        # 모든 보석을 하나 이상 포함할 때
        while len(dic) >= cnt:
            # 최솟값 갱신
            if j - i + 1 < res:
                res = j - i + 1
                answer = [i + 1, j + 1]

            # 왼쪽 포인터 감소
            dic[gems[i]] -= 1
            if dic[gems[i]] == 0:
                del dic[gems[i]]
            i += 1

    return answer