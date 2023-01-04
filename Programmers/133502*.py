# 프로그래머스 133502: 햄버거 만들기 (수정중))

def solution(ingredient):
    answer = 0
    ingredient = ''.join(str(i) for i in ingredient)

    while '1231' in ingredient:
        answer += 1
        ingredient = ingredient.replace('1231', '', 1) # 맨 앞의 기호만 교체 

    return answer

print(solution([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]))