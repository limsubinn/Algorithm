# 프로그래머스 152996: 시소 짝꿍

from collections import defaultdict

def solution(weights):
    answer = 0
    dic = defaultdict(int)  # 몸무게 : 해당 몸무게를 가진 사람의 수

    for w in weights:
        # 2m, 3m, 4m -> 몸무게 비율 1:1, 2:3, 1:2, 3:4
        answer += dic[w]
        answer += dic[2 * w] + dic[w / 2]
        answer += dic[(w * 2) / 3] + dic[(w * 3) / 2]
        answer += dic[(w * 3) / 4] + dic[(w * 4) / 3]
        # 자신의 몸무게
        dic[w] += 1

    return answer