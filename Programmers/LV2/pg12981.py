# 프로그래머스 12981: 영어 끝말잇기

def solution(n, words):
    answer = [1, 1]
    result = []

    for i in range(len(words)):
        # 중복된 단어
        if words[i] in result:
            return answer

        # 단어가 이어지지 않는 경우
        if i > 0 and words[i - 1][-1] != words[i][0]:
            return answer

        result.append(words[i])
        answer[0] += 1

        # 다음 턴
        if answer[0] > n:
            answer[0] = 1
            answer[1] += 1

    # 주어진 단어들로 탈락자가 생기지 않는 경우
    return [0, 0]