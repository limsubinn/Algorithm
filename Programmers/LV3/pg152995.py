# 프로그래머스 152995: 인사고과

def solution(scores):
    # 완호의 점수
    a, b = scores[0]
    # a 내림차순, b 오름차순
    scores.sort(key=lambda x: (-x[0], x[1]))

    answer = 1
    mb = 0
    for score in scores:
        # 완호가 인센티브를 받지 못하는 경우
        if a < score[0] and b < score[1]:
            return -1

        # 해당 사원이 인센티브를 받을 수 있는 경우
        if score[1] >= mb:
            # 최댓값 갱신
            mb = score[1]
            # 완호의 석차 증가
            if score[0] + score[1] > a + b:
                answer += 1

    return answer
