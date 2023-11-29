# 프로그래머스 131128: 숫자 짝꿍

def solution(X, Y):
    result = ''
    for i in range(9, -1, -1):
        num = str(i)
        result += num * min(X.count(num), Y.count(num))
   
    if result == "":
        return '-1'
    elif result[0] == "0":
        return '0'
    else:
        return result


'''
(실패)
입력받은 숫자를 리스트로 만들어서 역순으로 정렬해주고
반복문을 돌려 2개의 리스트(임의로 a, b)를 비교해서 숫자가 같으면 인덱스 둘다 넘어가고
a<b이면 b만 넘어가고, 반대의 경우에는 a만 넘어가게 하여 둘 중 하나의 인덱스가 끝나면 종료
-> 시간 초과 

(성공)
숫자 0~9를 기준으로 반복문을 돌려줬다. (큰 숫자를 구해야 하니 9 -> 0)
'''