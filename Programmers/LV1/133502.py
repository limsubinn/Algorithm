# 프로그래머스 133502: 햄버거 만들기

def solution(ingredient):
    answer = 0
    res = ''
    
    for i in ingredient:
        res += str(i)
        if res[-4:] == '1231':
            res = res[:-4]
            answer += 1

    return answer


'''
(실패)
입력 받은 배열을 스트링으로 바꿔서 '1231'이 포함되었을 때 그 부분을 제거하고 정답의 개수를 하나 추가 -> 시간 초과

(성공)
문자열을 하나 더 선언해서 ingredient의 값을 하나씩 넣어주고, 맨 끝의 문자열이 '1231'일 때 뒤에서 4개의 문자열을 지우고 정답의 개수를 하나 추가
'''