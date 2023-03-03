# 프로그래머스 72411: 메뉴 리뉴얼 (2021 KAKAO BLIND RECRUITMENT)

from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        result = {}
        for j in orders:
            # orders에서 course별로 해당 수 뽑아냄
            c = list(combinations(j, i))
            for k in c:
                # 알파벳 오름차순으로 정렬 후 문자열로 변환
                k = sorted(list(k))
                s = ''.join(k)
                # 딕셔너리에 추가 {문자열: 카운트}
                if s in result:
                    result[s] += 1
                else:
                    result[s] = 1
                    
        max_cnt = 0
        tmp = []
        for key in result:
            if result[key] < 2: # 2명 이하의 손님에게서 주문된 구성은 후보에 들어가지 않음
                continue

            if result[key] > max_cnt: # 최댓값 갱신
                max_cnt = result[key]
                tmp = [key]
            elif result[key] == max_cnt: # 동일한 최댓값 추가
                tmp.append(key)

        for i in tmp: # 정답 배열에 추가
            answer.append(i)

    answer.sort() # 알파벳 오름차순으로 정렬
    return answer