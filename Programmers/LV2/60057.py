# 프로그래머스 60057: 문자열 압축 (2020 KAKAO BLIND RECRUITMENT)

def solution(s):
    answer = 1000 # s의 최대 길이

    # 문자열의 길이의 절반만 탐색 (문자열의 길이가 1일 경우를 고려하여 +2)
    for i in range(1, len(s)//2+2):
        cnt = 1
        result = ''
        temp = ''

        # 문자열 압축
        for j in range(i, len(s)+1, i):
            if s[j-i:j] == temp:
                cnt += 1
            else:
                if cnt < 2:
                    result += temp
                else:
                    result += str(cnt) + temp
                cnt = 1
                temp = s[j-i:j]

        # 남은 문자열 전부 붙이기
        if cnt < 2:
            result += temp + s[j:]
        else:
            result += str(cnt) + temp + s[j:]

        # 최솟값 갱신
        answer = min(answer, len(result))

    return answer