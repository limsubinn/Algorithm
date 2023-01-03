# 프로그래머스 118666: 성격 유형 검사하기 (2022 KAKAO TECH INTERNSHIP)

def solution(survey, choices):
    answer = ''
    personalities = { "R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}

    for i in range(len(survey)):
        if choices[i] < 4:
            personalities[survey[i][0]] += (4 - choices[i])
        else:
            personalities[survey[i][1]] += (choices[i] - 4)

    keys = list(personalities.keys())
    values = list(personalities.values())
    
    for i in range(4):
        if values[2*i] >= values[2*i+1]:
            answer += keys[2*i]
        else:
            answer += keys[2*i+1]

    return answer