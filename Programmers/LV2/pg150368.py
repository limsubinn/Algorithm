# 프로그래머스 150368: 이모티콘 할인행사 (2023 KAKAO BLIND RECRUITMENT)

from itertools import product

def solution(users, emoticons):
    per = [10, 20, 30, 40] # 할인 케이스
    answer = [0, 0]
    
    for i in product(per, repeat=len(emoticons)): # 중복순열
        res = [0, 0]

        for rate, cost in users:
            total = 0 # 구매액 
            for j in range(len(emoticons)):
                if i[j] < rate: # rate보다 할인율이 큰 가격만 계산하도록 한다.
                    continue
                total += ((100 - i[j]) / 100) * emoticons[j]

            # 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 플러스 서비스에 가입
            if total >= cost:
                res[0] += 1
            else:
                res[1] += total

        # 조건1 -> 조건2 를 만족하는 최댓값 
        if answer[0] == res[0]:
            answer[1] = max(answer[1], res[1])
        elif answer[0] < res[0]:
            answer = res
    
    return answer