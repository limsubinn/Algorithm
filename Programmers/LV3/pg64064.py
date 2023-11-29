# 프로그래머스 64064: 불량 사용자

from itertools import product

def solution(user_id, banned_id):
    size = len(banned_id)

    # 불량 사용자 후보 찾기
    cases = [[] for _ in range(size)]
    for i in range(size):
        bid = banned_id[i]
        for uid in user_id:
            if len(bid) != len(uid):
                continue
            for j in range(len(bid)):
                if bid[j] == '*':
                    continue
                if bid[j] != uid[j]:
                    break
            else:
                cases[i].append(uid)

    result = []
    answer = 0
    for p in product(*cases): # 모든 경우의 수 탐색
        # 중복 제거
        s = set(p)
        # 불량 사용자 목록의 수보다 적은 경우 후보가 될 수 없다.
        if len(s) != size:
            continue
        for res in result:
            # 중복 제거
            if len(res - s) == 0:
                break
        # 후보가 될 수 있는 경우
        else:
            result.append(s)
            answer += 1

    return answer
